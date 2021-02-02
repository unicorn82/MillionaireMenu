from US.services.ScrapyService import ScrapyService
from US.services.MiracleService import MiracleService
from US.models.Dish import Dish
import json

import bs4


class DishMenuScrapy():
    def __init__(self):
        print('Collecting dish menu ...\n')

        self.dishes = []

    def collectDishes(self, index_id):
        baseUrl = "https://cn.investing.com/equities/StocksFilter?noconstruct=1&smlID=800&sid=&tabletype=price&index_id="+index_id
        # baseUrl = "https://cn.investing.com/equities/StocksFilter?noconstruct=1&smlID=800&sid=&tabletype=price&index_id=all"
        print("dishUrl= "+baseUrl)
        service = ScrapyService();
        response = service.callGetRequst(baseUrl, "")
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        trs_element = soup.select('#cross_rate_markets_stocks_1')[0].select('tr[id*="pair_"]')

        # trs_element = soup.select('tr[id*="pair_"]')

        backendService = MiracleService()

        # tr = trs_element[0]

        for tr in trs_element:
        # if tr is not None:

            pair_id = tr.get('id')
            href = tr.select('a[href]')[0].get('href')
            title = tr.select('a[href]')[0].get('title')
            dish = self.collectDishBasic(pair_id, href, title)


            #call backend to save
            # backendService.saveDishItem(dish)





    def collectDishBasic(self, pair_id, href, title):
        # href = "/equities/celesio-mu-historical-data"

        # / equities / el - paso - cor
        basic_url = "https://cn.investing.com"+href
        print("basic_url = " + basic_url)

        dish = Dish()
        dish.setCompanyName(title)
        dish.setCompany(href.replace("/equities/", ""))
        service = ScrapyService();
        basic_response = service.callGetRequst(basic_url, "")
        # print(basic_response.text)
        basic_soup = bs4.BeautifulSoup(basic_response.text, "html.parser")

        scripts_elements = basic_soup.findAll("script", {"type": "application/ld+json"});


        if len(scripts_elements) == 0:
            return

        script_json = json.loads(scripts_elements[0].text)
        dish.setTicker(script_json["tickersymbol"])
        # dish.setCompany(script_json["legalname"])



        dish_select_element = basic_soup.select('#DropDownContainer')[0].select('#DropdownBtn')[0].select('.btnTextDropDwn')[0]


        dish.setCategory(dish_select_element.text)


        overview_element = basic_soup.select('.overviewDataTable')[0]

        basic_elements = overview_element.findAll("div", {"class": "inlineblock"})



        self.collectHistoryDish(basic_soup.select('#pairSublinksLevel2')[0].findAll("li"), pair_id ,dish.ticker)



        for basic_ele in basic_elements:
            basic_attr = basic_ele.select('.float_lang_base_1')[0].text
            basic_value = basic_ele.select('.float_lang_base_2')[0].text
            # print(basic_attr+":"+basic_value)
            self.setDishBasicInfo(dish, basic_attr, basic_value)

        # print(dish.toJson())
        return dish

    def collectHistoryDish(self, historyLIs,  pair_id, ticker):
        # print(historyLIs)
        for li in historyLIs:

            if li.find('a') is not None and li.find('a').text == '历史数据':
                history_href = li.find('a').get('href')
                print(li.find('a').get('href'))
        historical_url = 'https://cn.investing.com'+history_href

        print(historical_url)
        json_o = self.findSmlId(historical_url)
        pairId = json_o['pairId']
        smlId = json_o['smlId']
        print(str(pairId)+" : "+str(smlId))
        service = ScrapyService()
        dish_price_list = service.getDishItemHistoryService(ticker,pairId, smlId)

        miracleService = MiracleService()

        miracleService.saveDishPriceHistory(dish_price_list)


        # print(basic_response.text)




        basic_url = "https://cn.investing.com/instruments/HistoricalDataAjax"
        service = ScrapyService();
        basic_response = service.callPostRequst(basic_url, "")


    def findSmlId(self, historical_url):
        service = ScrapyService();
        historical_response = service.callGetRequst(historical_url, "")
        historical_soup = bs4.BeautifulSoup(historical_response.text, "html.parser")
        for script in historical_soup.find_all('script'):
            if script.text.find('window.histDataExcessInfo')>0:
                json_string = script.text[script.text.find('=')+1:].strip().replace('pairId', '"pairId"').replace('smlId', '"smlId"')

                return json.loads(json_string)





    def setDishBasicInfo(self, dish, basic_attr, basic_value):
        if basic_attr == '营收':
            dish.setEarning(str(basic_value))
        if basic_attr == '52 周范围':
            dish.setW52Range(basic_value)
        if basic_attr == '每股收益':
            dish.setEPS(basic_value)
        if basic_attr == '市值':
            dish.setMarketCap(basic_value)
        if basic_attr == '股息':
            dish.setDividend(basic_value)
        if basic_attr == '平均成交量 (3个月)':
            dish.setAvg3mVolumn(basic_value)
        if basic_attr == '市盈率':
            dish.setPE(basic_value)
        if basic_attr == '贝塔':
            dish.setBeta(basic_value)
        if basic_attr == '1年涨跌幅':
            dish.setYearRange(basic_value)
        if basic_attr == '流通股份':
            dish.setCirMarketCap(basic_value)
        if basic_attr == '下一财报日':
            dish.setNextReportDate(basic_value)



    def collectAllUSDishes(self):
        # index_id = "14958"
        index_id = "all"
        # index_id = "27604"
        # category = "NASDAQ"
        self.collectDishes(index_id)


    def run(self):
        self.collectAllUSDishes();
        print('Collecting dish list ...\n')
