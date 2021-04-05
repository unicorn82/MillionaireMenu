from US.services.ScrapyService import ScrapyService
from US.services.MiracleService import MiracleService
from US.models.Index import Index
import traceback

class DishHistoryScrapy():
    def __init__(self):
        print('Collecting dish history ...\n')

        self.dishes = [
            {"ticker": "DJI","curr_id": "169", "smlID": "2030170", "description": "道琼斯工业平均指数"}, #道琼斯工业平均指数
            {"ticker": "HSI","curr_id": "179", "smlID": "2030179", "description": "恒生指数"}, #恒生指数
            {"ticker": "SPX", "curr_id": "166", "smlID": "2030167", "description": "标准普尔500指数"}, #标准普尔500指数
            {"ticker": "IXIC", "curr_id": "14958", "smlID": "2035302", "description": "纳斯达克综合指数"},  # 纳斯达克综合指数
            {"ticker": "NDX", "curr_id": "20", "smlID": "2030165", "description": "纳斯达克100指数"}, #纳斯达克100指数
            {"ticker": "SSE50", "curr_id": "995204", "smlID": "2144337", "description": "上证50指数"},  # 上证50指数
            {"ticker": "SSE", "curr_id": "40820", "smlID": "2057370", "description": "上证指数"},  # 上证指数
            {"ticker": "CSI300", "curr_id": "940801", "smlID": "2065987", "description": "沪深300指数"},  # 沪深300指数
            {"ticker": "CNT", "curr_id": "945512", "smlID": "2073873", "description": "创业板指数"},  # 创业板指数
            {"ticker": "CNT300", "curr_id": "945544", "smlID": "2074257", "description": "创业板300"}  # 创业板300



        ]
        self.st_date = "2007/01/01"
        self.end_date = "2021/03/07"


    def collectIndexHistory(self, obj):
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




    def run(self):
        for obj in self.dishes:
            print(obj["curr_id"]+" "+obj["smlID"])

            self.collectIndexHistory(obj);
        print('Collecting dish list ...\n')