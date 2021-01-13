import requests
import urllib3

class ScrapyService():
    def callGetRequst(self, requestUrl, queryParams):


        detail_response = requests.get(requestUrl, headers=self.generateRequestHeader(requestUrl), stream=True, timeout=30000, verify=False)


        # print(detail_response)
        # print("====="+detail_response.text)
        return detail_response;



    def generateRequestHeader(self, requestUrl):
        headers = {
            "Host": "cn.investing.com",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Referer": "https://cn.investing.com/equities/united-states",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Cookie": "logglytrackingsession=cf048a89-e995-44c7-9f04-13be83fce072; udid=cba0aa983acabba068234caff6370229; nyxDorf=Y2E%2FbzJ6MWw%2BbTk2N3owM2A4YjFjejEyMzNuaw%3D%3D; G_ENABLED_IDPS=google; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1609214632; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1609001685; OptanonConsent=isIABGlobal=false&datestamp=Mon+Dec+28+2020+21%3A03%3A51+GMT-0700+(MST)&version=6.7.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=US%3BCO; outbrain_cid_fetch=true; OptanonAlertBoxClosed=2020-12-29T04:03:50.007Z; _ga=GA1.2.1570956054.1609001684; _gat=1; _gid=GA1.2.141693151.1609212651; _gat_allSitesTracker=1; smd=cba0aa983acabba068234caff6370229-1609214452.550; __gads=ID=6c7292453afbee31-221ef5d373c50081:T=1609001686:RT=1609214335:S=ALNI_MZKz80-BqHvGqPVEdCQpJQzo1K4CA; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2226490%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A22%3A%22%2Fequities%2Ffacebook-inc%22%3B%7D%7D%7D%7D; adsFreeSalePopUp=3; logglytrackingsession=05191dde-12d2-4981-8696-79ef1609ef1d; geoC=US; adBlockerNewUserDomains=1609001681; PHPSESSID=4t8t0i1ev41enbp2gtcr51vuti; StickySession=id.39777004950.538.cn.investing.com"
            }

        return headers



