from US.utils.MathUtil import MathUtil
import re
class Index:

    @property
    def ticker(self):
        return self.__ticker

    def setTicker(self, value):
        self.__ticker = value

    @property
    def description(self):
            return self.__description

    def setDescription(self, value):
            self.__description = value

    def toJson(self):
        json = {}
        json['ticker'] = self.__ticker
        json['description'] = self.__description
        return json