from US.services.ScrapyService import ScrapyService
from US.services.MiracleService import MiracleService
from US.models.Index import Index
import traceback
import datetime

class DishHistoryScrapy():
    def __init__(self):
        print('Collecting dish history ...\n')
        self.isHistory = False
        self.dishes = [
            {"ticker": "DJI","curr_id": "169", "smlID": "2030170", "description": "道琼斯工业平均指数"}, #道琼斯工业平均指数
            #https://www.investing.com/indices/us-30-historical-data
            {"ticker": "HSI","curr_id": "179", "smlID": "2030179", "description": "恒生指数"}, #恒生指数
            #https: // www.investing.com / indices / hang - sen - 40 - historical - data
            {"ticker": "SPX", "curr_id": "166", "smlID": "2030167", "description": "标准普尔500指数"}, #标准普尔500指数
            #https://www.investing.com/indices/us-spx-500-historical-data
            {"ticker": "IXIC", "curr_id": "14958", "smlID": "2035302", "description": "纳斯达克综合指数"},  # 纳斯达克综合指数
            #https://www.investing.com/indices/nasdaq-composite-historical-data
            {"ticker": "NDX", "curr_id": "20", "smlID": "2030165", "description": "纳斯达克100指数"}, #纳斯达克100指数
            #https://www.investing.com/indices/nq-100-historical-data
            {"ticker": "SSE50", "curr_id": "995204", "smlID": "2144337", "description": "上证50指数"},  # 上证50指数
            #https://www.investing.com/indices/shanghai-se-50-historical-data
            {"ticker": "SSE", "curr_id": "40820", "smlID": "2057370", "description": "上证指数"},  # 上证指数
            #https: // www.investing.com / indices / shanghai - composite - historical - data
            {"ticker": "CSI300", "curr_id": "940801", "smlID": "2065987", "description": "沪深300指数"},  # 沪深300指数
            #https://www.investing.com/indices/csi300-historical-data
            {"ticker": "CNT", "curr_id": "945512", "smlID": "2073873", "description": "创业板指数"},  # 创业板指数
            #https://www.investing.com/indices/chinext-price-historical-data

            #https: // www.investing.com / indices / nyse - composite - historical - data NYSE



        ]

        self.st_date = "2007/01/01"






    def collectIndexHistory(self, obj):
        now = datetime.datetime.now()
        if not self.isHistory:
            self.st_date = now.strftime("%Y/01/01")
        post_url = "https://cn.investing.com/instruments/HistoricalDataAjax"
        service = ScrapyService()

        dish_price_list = service.getDishItemHistoryService(obj.get("ticker"), obj.get("curr_id"), obj.get("smlID"), self.st_date)

        miracleService = MiracleService()
        indexItem = Index();
        indexItem.setTicker(obj.get("ticker"))
        indexItem.setDescription(obj.get("description"))
        miracleService.saveIndexItem(indexItem)
        miracleService.saveIndexPriceHistory(dish_price_list)

        # miracleService.saveDishPriceHistory(dish_price_list)


    # curr_id: 169
    # smlID: 2030170
    # header: 道琼斯工业平均指数历史数据
    # st_date: 2010 / 01 / 01
    # end_date: 2021 / 03 / 07
    # interval_sec: Daily
    # sort_col: date
    # sort_ord: DESC
    # action: historical_data




    def run(self, isHistory):
        self.isHistory = isHistory
        for obj in self.dishes:
            print(obj["curr_id"]+" "+obj["smlID"])

            self.collectIndexHistory(obj);
        print('Collecting dish list ...\n')