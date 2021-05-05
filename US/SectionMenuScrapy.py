
from os import listdir
from os import walk
from os.path import isfile, join
import csv
import bs4
from US.models.DishPrice import DishPrice
from US.models.Index import Index
from datetime import datetime
from US.services.MiracleService import MiracleService
from US.services.ScrapyService import ScrapyService



class SectionMenuScrapy():
    def __init__(self):
        self.workDirectory = '/Users/eyin/index_history'
        self.miracleService = MiracleService()
        self.scrapyService = ScrapyService()
        self.dishes = [
            {"ticker": "DJI", "curr_id": "169", "smlID": "2030170", "url": "https://www.investing.com/indices/us-30-historical-data"},
            {"ticker": "HSI", "curr_id": "179", "smlID": "2030179",  "url": "https://www.investing.com/indices/hang-sen-40-historical-data"},
            {"ticker": "SPX", "curr_id": "166", "smlID": "2030167",  "url": "https://www.investing.com/indices/us-spx-500-historical-data" },
            {"ticker": "IXIC", "curr_id": "14958", "smlID": "2035302", "url": "https://www.investing.com/indices/nasdaq-composite-historical-data"},
            {"ticker": "NDX", "curr_id": "20", "smlID": "2030165", "url": "https://www.investing.com/indices/nq-100-historical-data"},
            {"ticker": "SSE50", "curr_id": "995204", "smlID": "2144337", "url": "https://www.investing.com/indices/shanghai-se-50-historical-data"},
            {"ticker": "SSEC", "curr_id": "40820", "smlID": "2057370", "url": "https://www.investing.com/indices/shanghai-composite-historical-data"},
            {"ticker": "CSI300", "curr_id": "940801", "smlID": "2065987", "url": "https://www.investing.com/indices/csi300-historical-data"},
            {"ticker": "CNT", "curr_id": "945512", "smlID": "2073873", "url": "https://www.investing.com/indices/chinext-price-historical-data"},
            {"ticker": "NYSE", "url": "https://www.investing.com/indices/nyse-composite-historical-data"},
            {"ticker": "S&P",  "url": "https://www.investing.com/indices/s-p-citic50-historical-data"},
            {"ticker": "NYA", "url": "https://www.investing.com/indices/nyse-composite-historical-data"},
            {"ticker": "SZI", "url": "https://www.investing.com/indices/szse-component-historical-data"}
        ]





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

    def scrapyIndexHistory(self):
        for indexObject in self.dishes:
            print(indexObject["url"])
            ticker = indexObject["ticker"]
            response = self.scrapyService.callGetRequst(indexObject["url"], "")
            # print(response.text)
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            if soup.select('#curr_table') is not None:
                table_element = soup.select('#curr_table')[0]
                trs_element = table_element.select('tr')
                dist_list = []
                for tr in trs_element:
                    dishModel = self.packDishPriceFromTr(tr, ticker)
                    if dishModel is not None:
                        dist_list.append(dishModel.toJson())
                        print(dishModel.toJson())
            self.miracleService.saveTickerIndexPriceHistory(ticker, dist_list)




    def packDishPriceFromTr(self, tr, ticker):
        dishModel = DishPrice()
        dishModel.setTicker(ticker)
        tds = tr.select('td')
        if len(tds) == 7:
            dishModel.setDate(datetime.strptime(tds[0].text, '%b %d, %Y').strftime('%m/%d/%Y'))
            dishModel.setClose(tds[1].text)
            dishModel.setOpen(tds[2].text)
            dishModel.setHigh(tds[3].text)
            dishModel.setLow(tds[4].text)
            dishModel.setVolume(tds[5].text)
            dishModel.setRange(tds[6].text)
            return dishModel
        else:
            return None









    def run(self, history):
        if history:
            self.loopAllHistoryFiles()
        else:
            self.scrapyIndexHistory()

print("----------")
section = SectionMenuScrapy()
section.run(False)
