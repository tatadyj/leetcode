#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)

        if not self.stack or self.arr[self.stack[-1]] > price:
            res = 1
        else:
            # prev smaller or equal 
            while self.stack and self.arr[self.stack[-1]] <= price:
                self.stack.pop()
            if not self.stack:
                res = len(self.arr)
            else:
                res = len(self.arr) - 1 - self.stack[-1]

        self.stack.append(len(self.arr)-1) 
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

