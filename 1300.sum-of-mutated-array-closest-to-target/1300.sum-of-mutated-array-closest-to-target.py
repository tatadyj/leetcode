#
# @lc app=leetcode id=1300 lang=python3
#
# [1300] Sum of Mutated Array Closest to Target
#

# @lc code=start
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def get_sum(val):
            return sum([min(v, val) for v in arr])

        if sum(arr) <= target:
            return max(arr)

        left = 0
        right = max(arr)

        while left + 1 < right:
            mid = (left + right) // 2
            val = get_sum(mid)
            if val >= target:
                right = mid 
            else:
                left = mid 
        lval = abs(get_sum(left) - target)
        rval = abs(get_sum(right) - target)
    
        if lval <= rval:
            return left
        else:
            return right        
# @lc code=end

