#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def count_x(val):
            count = 0
            for n in nums:
                if n >= val:
                    count += 1
            return count

        left = 1
        right = len(nums)

        while left < right:
            mid = (left + right + 1) // 2
            count = count_x(mid)
            if count < mid:
                right = mid - 1
            else:
                left = mid 

        if count_x(left) == left:
            return left 
        return -1
        
        
# @lc code=end

