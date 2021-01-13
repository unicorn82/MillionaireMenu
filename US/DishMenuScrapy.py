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
        print("baseUrl= "+baseUrl)
        service = ScrapyService();
        response = service.callGetRequst(baseUrl, "")
        # print(response.text)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        trs_element = soup.select('#cross_rate_markets_stocks_1')[0].select('tr[id*="pair_"]')

        # trs_element = soup.select('tr[id*="pair_"]')

        backendService = MiracleService()

        # tr = trs_element[0]

        for tr in trs_element:
        # if tr is not None:
            print(tr)
            pair_id = tr.get('id')
            href = tr.select('a[href]')[0].get('href')
            title = tr.select('a[href]')[0].get('title')
            dish = self.collectDishBasic(pair_id, href, title)

            backendService.saveDishItem(dish)



    def collectDishBasic(self, pair_id, href, title):
        # href = "/equities/el-paso-cor"

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
        print(scripts_elements[0].text)
        script_json = json.loads(scripts_elements[0].text)
        dish.setTicker(script_json["tickersymbol"])
        # dish.setCompany(script_json["legalname"])



        dish_select_element = basic_soup.select('#DropDownContainer')[0].select('#DropdownBtn')[0].select('.btnTextDropDwn')[0]

        print(dish_select_element.text)
        dish.setCategory(dish_select_element.text)


        overview_element = basic_soup.select('.overviewDataTable')[0]

        basic_elements = overview_element.findAll("div", {"class": "inlineblock"})



        for basic_ele in basic_elements:
            basic_attr = basic_ele.select('.float_lang_base_1')[0].text
            basic_value = basic_ele.select('.float_lang_base_2')[0].text
            print(basic_attr+":"+basic_value)
            self.setDishBasicInfo(dish, basic_attr, basic_value)




        print(dish.toJson())
        return dish

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
