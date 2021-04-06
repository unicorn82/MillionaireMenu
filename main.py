from US.DishMenuScrapy import DishMenuScrapy
from US.DishHistoryScrapy import DishHistoryScrapy
from US.StockMenuScrapy import StockMenuScrapy
from decimal import Decimal
from US.utils.MathUtil import MathUtil
import sys
import re

def main():
    print('Millionaire Menu is delivering...\n')
    # args = option.parser.parse_args()
    # dish = DishMenuScrapy();
    # dish.run()


    if len(sys.argv) >1 and sys.argv[1] == "history":
        # history = DishHistoryScrapy()
        # history.run(True)
        dish = StockMenuScrapy()
        dish.run(bool(True))
    else:
        history = DishHistoryScrapy()
        history.run(False)
        dish = StockMenuScrapy()
        dish.run(bool(False))







    print('Millionaire Menu is done...\n')

if __name__ == '__main__':
    main()