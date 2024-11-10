#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def is_valid(val):
            idx = bisect_left(citations, val)
            if len(citations) - idx >= val:
                return True 
            else:
                return False 
                
        left = 0 
        right = max(citations)

        while left + 1 < right:
            mid = (left + right) // 2
            if is_valid(mid):
                left = mid 
            else:
                right = mid 

        if is_valid(right):
            return right 
        else:
            return left        
# @lc code=end

