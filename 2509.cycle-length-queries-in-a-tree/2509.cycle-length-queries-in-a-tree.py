#
# @lc app=leetcode id=2509 lang=python3
#
# [2509] Cycle Length Queries in a Tree
#

# @lc code=start
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # p的父节点 p//2
        # p，q 不断往上找父节点，知道p，q汇合 
        # 每次往上移动，edge数+1 
        ans = []
        for p, q in queries:
            count = 0
            while p != q:
                if p > q:
                    p = p // 2 
                    count += 1
                else:
                    q = q // 2
                    count += 1

            ans.append(count + 1)
        return ans
            
        
# @lc code=end

