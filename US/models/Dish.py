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
    def company(self):
        return self.__company

    def setCompany(self, value):
        self.__company = value

    @property
    def companyName(self):
        return self.__companyName

    def setCompanyName(self, value):
        self.__companyName = value

    @property
    def avg3mVolumn(self):
        return self.__avg3mVolumn

    def setAvg3mVolumn(self, value):
        if value != "N/A":
            self.__avg3mVolumn = MathUtil.text_to_num(value)
        else:
            self.__avg3mVolumn = -1.0

    @property
    def yearRange(self):
        return self.__yearRange

    def setYearRange(self, value):
        if value != "N/A":
            self.__yearRange = MathUtil.p2f(value)
        else:
            self.__yearRange = -1.0

    @property
    def w52Range(self):
        return self.__w52Range

    def setW52Range(self, value):
        self.__w52Range = value

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
    def cirMarketCap(self):
        return self.__cirMarketCap

    def setCirMarketCap(self, value):
        if value != "N/A":
            self.__cirMarketCap = MathUtil.text_to_num(value)
        else:
            self.__cirMarketCap = -1

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
            self.__EPS = value
        else:
            self.__EPS = -1

    @property
    def dividend(self):
        return self.__dividend

    def setDividend(self, value):
        if value.find('N/A') < 0:

            self.__dividend = (float(value.split("(")[0]))
            self.__yield = MathUtil.p2f(value.split("(")[1].split(")")[0])
        # self.__dividend = value

    @property
    def beta(self):
        return self.__beta

    def setBeta(self, value):
        if value != "N/A":
            self.__beta = float(value.replace(' ',''))
        else:
            self.__beta = -1

    @property
    def nextReportDate(self):
        return self.__nextReportDate

    def setNextReportDate(self, value):
        self.__nextReportDate = value.replace('年','-').replace('月', '-').replace('日', '')



    def __init__(self):
        self.__ticker = ''
        self.__category = ''
        self.__company = ''
        self.__companyName = ''
        self.__avg3mVolumn = 0
        self.__yearRange = 0.0
        self.__w52Range = 0.0
        self.__marketCap = 0
        self.__PE = 0.0
        self.__cirMarketCap = 0  # circulation market
        self.__earning = 0
        self.__EPS = 0.0 #
        self.__forwardDividend = 0.0
        self.__yield = 0.0
        self.__beta = 0.0
        self.__nextReportDate = ''
        self.__dividend = 0.0

    # def fromJson(self, json):
    #     return


    def toJson(self):
        json = {}
        json['ticker'] = self.__ticker
        json['category'] = self.__category
        json['company'] = self.__company
        json['companyName'] = self.__companyName
        json['avg3mVolumn'] = self.__avg3mVolumn
        json['yearRange'] = self.__yearRange
        json['w52Range'] = self.__w52Range
        json['marketCap'] = self.__marketCap
        json['PE'] = self.__PE
        json['EPS'] = self.__EPS
        json['cirMarketCap'] = self.__cirMarketCap
        json['earning'] = self.__earning
        json['dividend'] = self.__dividend
        json['yield'] = self.__yield
        json['beta'] = self.__beta
        json['nextReportDate'] = self.__nextReportDate

        return json
