#
# @lc app=leetcode id=710 lang=python3
#
# [710] Random Pick with Blacklist
#

# @lc code=start
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.size = n - len(blacklist)
        self.map = {}
        lastIdx = n - 1
        for b in blacklist:
            self.map[b] = lastIdx
            lastIdx -= 1 
        

    def pick(self) -> int:
        idx = random.randint(0, )
        if idx in self.map:
            return self.map[idx]
        return idx 


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
# @lc code=end

