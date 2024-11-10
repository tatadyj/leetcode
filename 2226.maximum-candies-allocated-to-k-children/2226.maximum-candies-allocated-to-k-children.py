#
# @lc app=leetcode id=2226 lang=python3
#
# [2226] Maximum Candies Allocated to K Children
#

# @lc code=start
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def is_valid(val):
            if sum(candies) < k*val:
                return False 

            count = 0
            for c in candies:
                if c >= val:
                    count += floor(c/val)
            return count >= k



        left = 0
        right = max(candies)
        while left < right:
            mid = (left + right + 1) // 2
            if is_valid(mid):
                left = mid 
            else:
                right = mid - 1
        return left  
# @lc code=end

