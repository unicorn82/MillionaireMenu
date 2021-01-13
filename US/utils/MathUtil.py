from decimal import Decimal


class MathUtil():
    def __init__(self):
        self.d = {
            'M': 6,
            'B': 9
        }

    @staticmethod
    def text_to_num(text):
        d = {
            'K': 3,
            'M': 6,
            'B': 9,
            'T': 12
        }
        text = text.replace(',', '').replace(' ','')
        if text[-1] in d:
            num, magnitude = text[:-1], text[-1]
            return int(Decimal(str(num)) * 10 ** d[magnitude])
        else:
            return int(Decimal(text))

    # @staticmethod
    # def text_remove_comma(text):
    #
    #     return int(text.replace(',', '').replace(' ',''))

    @staticmethod
    def p2f(text):
        if text != "N/A":
            return float(text.replace(" ","").strip('%')) / 100
        else:
            return -1.0


