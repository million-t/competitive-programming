class StockSpanner:

    def __init__(self):
        self.stock_prices = []
        self.stack = []
        

    def next(self, price: int) -> int:
        self.stock_prices.append(price)
        len_stock_prices = len(self.stock_prices)
    
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        
        if self.stack:
            span = len_stock_prices - 1 - self.stack[-1][1]
        
        else:
            span = len_stock_prices
        self.stack.append([price, len_stock_prices - 1])

        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)