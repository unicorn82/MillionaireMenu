
from os import listdir
from os import walk
from os.path import isfile, join
import csv
from US.models.DishPrice import DishPrice
from US.models.Index import Index
from datetime import datetime
from US.services.MiracleService import MiracleService



class SectionMenuScrapy():
    def __init__(self):
        self.workDirectory = '/Users/eyin/index_history'
        self.miracleService = MiracleService()

    def loopAllHistoryFiles(self):
        _, _, filenames = next(walk(self.workDirectory))

        for file in filenames:
            if not file.endswith("csv"):
                continue

            dish_prices = []
            indexModel = Index()
            ticker = file[:file.index('_')]
            description = file[file.index('_')+1:file.index('.csv')]
            indexModel.setTicker(ticker)
            indexModel.setDescription(description)

            print(indexModel.toJson())
            with open(self.workDirectory+'/'+file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count != 0:
                        dishModel = self.packRow2Model(row, ticker)
                        dish_prices.append(dishModel.toJson())
                    line_count = line_count+1
                self.miracleService.saveIndexItem(indexModel)
                self.miracleService.saveIndexPriceHistory(dish_prices)

    def packRow2Model(self, row, ticker):
        dishModel = DishPrice()
        dishModel.setTicker(ticker)
        if len(row) == 7:

            dishModel.setDate(datetime.strptime(row[0], '%b %d, %Y').strftime('%m/%d/%Y'))
            dishModel.setClose(row[1])
            dishModel.setOpen(row[2])
            dishModel.setHigh(row[3])
            dishModel.setLow(row[4])
            dishModel.setVolume(row[5])
            dishModel.setRange(row[6])

            print(dishModel.toJson())
        return dishModel


    def run(self, history):
        if history:
            self.loopAllHistoryFiles()

print("----------")
section = SectionMenuScrapy()
section.run(True)
