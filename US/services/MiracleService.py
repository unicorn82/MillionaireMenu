# importing the requests library
import requests

# defining the api-endpoint
# MIRACLE_API_ENDPOINT = "http://pp-cacl-data.flatironssolutions.com:8080/service/"

MIRACLE_API_ENDPOINT = "http://localhost:8080/service/"

class MiracleService():

    def callPostRequest(self, service, payload):
        # sending post request and saving response as response object
        print("Send post request "+MIRACLE_API_ENDPOINT+service)
        r = requests.post(url=MIRACLE_API_ENDPOINT+service, json=payload, headers=self.generateRequestHeader())

        print(r.status_code)
        # extracting response text
        pastebin_url = r.text
        print("The pastebin URL is:%s" % pastebin_url)



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
        print(payload)
        self.callPostRequest(service, payload)

    def saveDishPriceHistory(self, ticker, dish_price_list):
        service = "stock/price/"+ticker+"/save"
        payload = dish_price_list
        print(payload)
        self.callPostRequest(service, payload)
        return

    def saveIndexItem(self, index):
        service = "index/save"
        payload = index.toJson()
        print(payload)
        self.callPostRequest(service, payload)

    def saveIndexPriceHistory(self, index_price_list):
        service = "index/price/save"
        payload = index_price_list
        self.callPostRequest(service, payload)
        return






