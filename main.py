from US.DishMenuScrapy import DishMenuScrapy
from decimal import Decimal
from US.utils.MathUtil import MathUtil
import re

def main():
    print('Millionaire Menu is delivering...\n')
    # args = option.parser.parse_args()
    dish = DishMenuScrapy();
    dish.run()

    # print(Decimal('78.1') * 10)
    # print(Decimal('24,841,969'))

    text = '- 15.55 % '
    print(MathUtil.p2f(text))






    print('Millionaire Menu is done...\n')

if __name__ == '__main__':
    main()