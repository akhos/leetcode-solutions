from collections import deque
class StockSpanner:
    def __init__(self):
        self.stStack = deque()
        self.spanStack = deque()
        
    def next(self, price: int) -> int:
        counter = 1
        while self.stStack and self.stStack[-1] <= price:
            self.stStack.pop()
            counter += self.spanStack.pop()
        self.stStack.append(price)
        self.spanStack.append(counter)
        return counter