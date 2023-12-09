class Risk:
    def __init__(self, symbol: str, ratio: float, eval: str):
        self.symbol = symbol
        self.ratio = ratio
        self.eval = eval

    def set_symbol(self, symbol: str):
        self.symbol = symbol

    def set_ratio(self, ratio: float):
        self.ratio = ratio

    def set_eval(self, eval: str):
        self.eval = eval