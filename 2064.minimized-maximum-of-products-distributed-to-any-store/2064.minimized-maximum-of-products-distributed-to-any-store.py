#
# @lc app=leetcode id=2064 lang=python3
#
# [2064] Minimized Maximum of Products Distributed to Any Store
#

# @lc code=start
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def is_ok(max_val):
            if max_val > max(quantities):
                return False 

            count = 0
            for q in quantities:
                count += ceil(q/max_val)
            return count <= n 

        left = 1
        right = max(quantities)
        while left < right:
            mid = (left + right) // 2
            if is_ok(mid):
                right = mid 
            else:
                left = mid + 1
        return left
        
# @lc code=end

