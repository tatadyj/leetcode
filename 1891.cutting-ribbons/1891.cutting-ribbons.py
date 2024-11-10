#
# @lc app=leetcode id=1891 lang=python3
#
# [1891] Cutting Ribbons
#

# @lc code=start
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def count(len):
            count = 0
            for r in ribbons:
                count += r // len
            return count

        left = 1
        right = max(ribbons)
        while left < right:
            mid = (left + right + 1) // 2
            if count(mid) >= k:
                left = mid 
            else:
                right = mid - 1
        
        ret = count(left)
        if ret >= k:
            return left 
        else:
            return 0 
        
# @lc code=end

