from US.DishMenuScrapy import DishMenuScrapy
from US.DishHistoryScrapy import DishHistoryScrapy
from decimal import Decimal
from US.utils.MathUtil import MathUtil
import sys
import re

def main():
    print('Millionaire Menu is delivering...\n')
    # args = option.parser.parse_args()
    # dish = DishMenuScrapy();
    # dish.run()

    print(sys.argv[1])
    if sys.argv[1] == "history":
        history = DishHistoryScrapy()
        history.run()
    else:
        dish = DishMenuScrapy();
        dish.run()







    print('Millionaire Menu is done...\n')

if __name__ == '__main__':
    main()