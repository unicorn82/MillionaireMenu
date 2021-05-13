# importing the requests library
import requests
from utils.logging import logHelper

# defining the api-endpoint
# MIRACLE_API_ENDPOINT = "http://pp-cacl-data.flatironssolutions.com:8080/service/"

MIRACLE_API_ENDPOINT = "http://localhost:8080/service/"

class MiracleService():

    def __init__(self):
        module = 'service'
        self.logger = logHelper(module)


    def callPostRequest(self, service, payload):
        # sending post request and saving response as response object
        self.logger.info("Send post request "+MIRACLE_API_ENDPOINT+service)
        r = requests.post(url=MIRACLE_API_ENDPOINT+service, json=payload, headers=self.generateRequestHeader())

        self.logger.info(r.status_code)
        # extracting response text
        pastebin_url = r.text
        self.logger.info("The pastebin URL is:%s" % pastebin_url)



    def generateRequestHeader(self):
        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            'Accept-Encoding': 'gzip,deflate'

        }
        return headers

    def saveDishItem(self, dish):
        service = "stock/save"
        payload = dish.toJson()
        self.logger.info(payload)
        # self.callPostRequest(service, payload)

    def saveDishPriceHistory(self, ticker, dish_price_list):
        service = "stock/price/"+ticker+"/save"
        payload = dish_price_list
        # self.callPostRequest(service, payload)
        return

    def saveIndexItem(self, index):
        service = "index/save"
        payload = index.toJson()
        # self.callPostRequest(service, payload)

    def saveIndexPriceHistory(self, index_price_list):
        service = "index/price/save"
        payload = index_price_list
        # self.callPostRequest(service, payload)
        return

    def saveTickerIndexPriceHistory(self, ticker, index_price_list):
        service = "index/price/"+ticker+"/save"
        payload = index_price_list
        # self.callPostRequest(service, payload)
        return






