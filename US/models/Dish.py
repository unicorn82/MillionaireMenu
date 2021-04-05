from US.utils.MathUtil import MathUtil
import re
class Dish:


    @property
    def ticker(self):
        return self.__ticker

    def setTicker(self, value):
        self.__ticker = value

    @property
    def category(self):
        return self.__category

    def setCategory(self, value):
            self.__category = value

    @property
    def sector(self):
        return self.__sector

    def setSector(self, value):
        self.__sector = value

    @property
    def companyName(self):
        return self.__companyName

    def setCompanyName(self, value):
        self.__companyName = value

    @property
    def industry(self):
        return self.__industry

    def setIndustry(self, value):
        self.__industry = value

    @property
    def oneYrTarget(self):
        return self.__oneYrTarget

    def setOneYrTarget(self, value):
        if value != 'N/A':
            self.__oneYrTarget = float(MathUtil.text_to_num(value))



    @property
    def marketCap(self):
        return self.__marketCap

    def setMarketCap(self, value):
        if value != "N/A":
            self.__marketCap = MathUtil.text_to_num(value)
        else:
            self.__marketCap = -1.0

    @property
    def PE(self):
        return self.__PE

    def setPE(self, value):
        if value != "N/A":
            self.__PE = float(value)
        else:
            self.__PE = -1.0

    @property
    def forwardPE1Yr(self):
        return self.__forwardPE1Yr
    def setForwardPE1Yr(self, value):
        self.__forwardPE1Yr = value



    @property
    def earning(self):
        return self.__earning

    def setEarning(self, value):
        if value != "N/A":
            self.__earning = MathUtil.text_to_num(value)
        else:
            self.__earning = -1

    @property
    def EPS(self):
        return self.__EPS

    def setEPS(self, value):
        if value != "N/A":
            self.__EPS = float(MathUtil.text_to_num(value))
        else:
            self.__EPS = -1

    @property
    def dividend(self):
        return self.__dividend

    def setDividend(self, value):
        if value.find('N/A') < 0:
            self.__dividend = value

            # self.__dividend = (float(value.split("(")[0]))
            # self.__yield = MathUtil.p2f(value.split("(")[1].split(")")[0])
        # self.__dividend = value

    @property
    def dividend(self):
        return self.__dividend

    def setDividend(self, value):
        if value.find('N/A') < 0:
            self.__dividend = MathUtil.text_to_num(value)


    @property
    def getYield(self):
        return self.__yield

    def setYield(self, value):
        if value.find('N/A') < 0:
            self.__yield = MathUtil.p2f(value)

    @property
    def beta(self):
        return self.__beta

    def setBeta(self, value):
        self.__beta = value

    @property
    def nextReportDate(self):
        return self.__nextReportDate

    def setNextReportDate(self, value):
        self.__nextReportDate = value.replace('年','-').replace('月', '-').replace('日', '')

    @property
    def url(self):
        return self.__url

    def setUrl(self, value):
            self.__url = value





    def __init__(self):
        self.__ticker = ''
        self.__category = ''
        self.__sector = ''
        self.__companyName = ''
        self.__industry = ''
        self.__oneYrTarget = ''
        self.__marketCap = 0
        self.__PE = 0.0
        self.__forwardPE1Yr = 0.0

        self.__earning = 0
        self.__EPS = 0.0 #
        self.__forwardDividend = 0.0
        self.__yield = 0.0
        self.__beta = 0.0
        self.__nextReportDate = ''
        self.__dividend = 0.0
        self.__url = ''

    # def fromJson(self, json):
    #     return


    def toJson(self):
        json = {}
        json['ticker'] = self.__ticker
        json['category'] = self.__category
        json['sector'] = self.__sector
        json['companyName'] = self.__companyName
        json['industry'] = self.__industry
        json['oneYrTarget'] = self.__oneYrTarget
        json['forwardPE1Yr'] = self.__forwardPE1Yr

        json['marketCap'] = self.__marketCap
        json['PE'] = self.__PE
        json['EPS'] = self.__EPS

        json['earning'] = self.__earning
        json['dividend'] = self.__dividend
        json['yield'] = self.__yield
        json['beta'] = self.__beta
        json['nextReportDate'] = self.__nextReportDate
        json['url'] = self.__url

        return json
