#
# @lc app=leetcode id=497 lang=python3
#
# [497] Random Point in Non-overlapping Rectangles
#

# @lc code=start
import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.count = []
        for a, b, x, y in rects:
            self.count.append((x-a+1)*(y-b+1))
        for i in range(1, len(self.count)):
            self.count[i] += self.count[i-1]

    def pick(self) -> List[int]:
        rnd = random.randint(1, self.count[-1])
        idx = bisect.bisect_left(self.count, rnd)
        if idx > 0:
            rnd -= self.count[idx-1]
        rnd -= 1 # 对于一个rect，从0开始计数
        x1, y1, x2, y2 = self.rects[idx]
        ncol = y2 - y1 + 1 
        irow = rnd // ncol 
        icol = rnd % ncol
        return [x1 + irow, y1 + icol]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# @lc code=end

