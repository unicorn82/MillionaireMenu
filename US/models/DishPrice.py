from US.utils.MathUtil import MathUtil
import re
class DishPrice:

    @property
    def ticker(self):
        return self.__ticker

    def setTicker(self, value):
        self.__ticker = value

    @property
    def date(self):
        return self.__date

    def setDate(self, value):
        self.__date = value
        # self.__date = value.replace('年','-').replace('月', '-').replace('日', '')

    @property
    def open(self):
        return self.__open
    def setOpen(self, value):
        self.__open = float(MathUtil.text_to_num(value))

    @property
    def close(self):
        return self.__close
    def setClose(self, value):
        self.__close = float(MathUtil.text_to_num(value))

    @property
    def high(self):
        return self.__high
    def setHigh(self, value):
        self.__high = float(MathUtil.text_to_num(value))

    @property
    def low(self):
        return self.__low
    def setLow(self, value):
        self.__low = float(MathUtil.text_to_num(value))

    @property
    def volume(self):
        return self.__volume

    def setVolume(self, value):
        if value != '-':
            self.__volume = MathUtil.text_to_num(value)

    @property
    def range(self):
        return self.__range

    def setRange(self, value):
        self.__range = MathUtil.p2f(value)



    def __init__(self):
        self.__ticker = ''
        self.__date = ''
        self.__open = 0.0
        self.__close = 0.0
        self.__high = 0.0
        self.__low = 0.0
        self.__volume = 0
        self.__range = 0.0

    def toJson(self):
        json = {}
        json['ticker'] = self.ticker
        json['date'] = self.date
        json['open'] = self.open
        json['close'] = self.close
        json['high'] = self.high
        json['low'] = self.low
        json['volume'] = self.volume
        json['range'] = self.range
        return json