import json
import bs4
import requests
import urllib3

import datetime
from US.models.Dish import Dish
from US.models.DishPrice import DishPrice
from US.services.MiracleService import MiracleService
from utils.logging import logHelper

class StockMenuScrapy():
    def __init__(self):
        print('Collecting dish menu ...\n')
        self.module = 'scrapy'
        self.dishes = []
        self.isHistory = False
        self.miracleService = MiracleService()
        self.logger = logHelper(self.module)

    def collectAllUSDishes(self):
        exchanges = ['NASDAQ', 'NYSE', 'AMEX']
        offset = 0
        limit = 100
        for ex in exchanges:
            while(True):
                screener_url = 'https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit='+str(limit)+'&offset='+str(offset)+'&exchange='+ex
                self.logger.info(screener_url)
                screener_response = self.callGetRequst(screener_url)
                if self.packDishList(screener_response.json(), ex) == 0:
                    break
                # self.packDishList(json.loads(screener_response.json()))
                # print(screener_response.text)
                offset += limit

    def collectDishSummary(self, symbol):
        info_url = 'https://api.nasdaq.com/api/quote/'+symbol+'/summary?assetclass=stocks'
        self.logger.info(info_url)
        info_response = self.callGetRequst(info_url)


        return info_response.json()['data']


    def packDishList(self, jsonObj, exchange):
        rows = jsonObj['data']['table']['rows']
        if rows == None:
            return 0
        for row in rows:
            # print(row)
            ticker = row['symbol']
            dish = self.packDish(row)

            if dish != None:
                self.logger.debug(dish.toJson())
                self.dishes.append(dish)

                self.miracleService.saveDishItem(dish)


            dish_prices = self.packDishPrice(ticker)
            self.miracleService.saveDishPriceHistory(ticker, dish_prices)
            self.logger.info(dish_prices)
        return len(rows)

    def packDish(self, row):
        dishSummary = self.collectDishSummary(row['symbol'])
        if dishSummary == None:
            return None
        infoObj = dishSummary['summaryData']
        dish = Dish()
        dish.setTicker(row['symbol'])
        dish.setCompanyName(row['name'])
        dish.setUrl(row['url'])
        dish.setCategory(infoObj['Exchange']['value'])
        dish.setSector(infoObj['Sector']['value'])
        dish.setIndustry(infoObj['Industry']['value'])
        dish.setOneYrTarget(infoObj['OneYrTarget']['value'])
        dish.setMarketCap(infoObj['MarketCap']['value'])
        dish.setPE(infoObj['PERatio']['value'])
        dish.setForwardPE1Yr(infoObj['ForwardPE1Yr']['value'])
        dish.setEPS(infoObj['EarningsPerShare']['value'])
        dish.setDividend(infoObj['AnnualizedDividend']['value'])
        dish.setYield(infoObj['Yield']['value'])
        dish.setBeta(infoObj['Beta']['value'])

        return dish

    def packDishPrice(self, ticker):
        now = datetime.datetime.now()
        fromdate = now.strftime("%Y-01-01")
        limit = 100
        offset = 0
        dish_prices = []
        if self.isHistory:
            fromdate = '2010-01-01'
        todate = now.strftime("%Y-%m-%d")
        self.logger.debug(fromdate)
        price_url = 'https://api.nasdaq.com/api/quote/'+str(ticker)+'/historical?assetclass=stocks&'\
                    +'fromdate='+fromdate+'&todate='+todate+'&limit='+str(limit)
        self.logger.info(price_url)
        init_response = self.callGetRequst(price_url)
        try:
            total_record = init_response.json()['data']['totalRecords']
            offset = total_record - limit
            if total_record < limit: 
                offset = 0
        
       
            while(not offset < 0):
                self.logger.info(price_url+'&offset='+str(offset))
                offset_response = self.callGetRequst(price_url+'&offset='+str(offset))
                self.packOffsetDishPrice(ticker, offset_response.json(), dish_prices)
                if(offset > limit):
                    offset = offset - limit
                else:
                    if offset > 0:
                        offset = 0
                    else:
                        offset = -1 #break the loop
        except:
            self.logger.error("Got Error")
        return dish_prices



    def packOffsetDishPrice(self, ticker, offset_response, dish_prices):
        if offset_response['data'] is not None:
            rows = offset_response['data']['tradesTable']['rows']

            for row in rows[::-1]:
                dish_price = DishPrice()
                dish_price.setTicker(ticker)
                dish_price.setDate(row['date'])
                dish_price.setOpen(row['open'])
                dish_price.setClose(row['close'])
                dish_price.setHigh(row['high'])
                dish_price.setLow(row['low'])
                dish_price.setVolume(row['volume'])
                dish_prices.append(dish_price.toJson())



    def callGetRequst(self, requestUrl):
        detail_response = requests.get(requestUrl, headers=self.generateRequestHeader())
        return detail_response


    def generateRequestHeader(self):
        headers = {
            "Connection": "keep-alive",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Cookie": "logglytrackingsession=cf048a89-e995-44c7-9f04-13be83fce072; udid=cba0aa983acabba068234caff6370229; nyxDorf=Y2E%2FbzJ6MWw%2BbTk2N3owM2A4YjFjejEyMzNuaw%3D%3D; G_ENABLED_IDPS=google; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1609214632; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1609001685; OptanonConsent=isIABGlobal=false&datestamp=Mon+Dec+28+2020+21%3A03%3A51+GMT-0700+(MST)&version=6.7.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=US%3BCO; outbrain_cid_fetch=true; OptanonAlertBoxClosed=2020-12-29T04:03:50.007Z; _ga=GA1.2.1570956054.1609001684; _gat=1; _gid=GA1.2.141693151.1609212651; _gat_allSitesTracker=1; smd=cba0aa983acabba068234caff6370229-1609214452.550; __gads=ID=6c7292453afbee31-221ef5d373c50081:T=1609001686:RT=1609214335:S=ALNI_MZKz80-BqHvGqPVEdCQpJQzo1K4CA; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2226490%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A22%3A%22%2Fequities%2Ffacebook-inc%22%3B%7D%7D%7D%7D; adsFreeSalePopUp=3; logglytrackingsession=05191dde-12d2-4981-8696-79ef1609ef1d; geoC=US; adBlockerNewUserDomains=1609001681; PHPSESSID=4t8t0i1ev41enbp2gtcr51vuti; StickySession=id.39777004950.538.cn.investing.com"
            }

        return headers


    def run(self, isHistory):
        self.isHistory = isHistory
        self.collectAllUSDishes();

        self.logger.info('Collecting dish list ...\n')

