#
# @lc app=leetcode id=2334 lang=python3
#
# [2334] Subarray With Elements Greater Than Varying Threshold
#

# @lc code=start
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(0)
        nums.insert(0, 0)
        stack = []
        res = -1

        # next left/right smaller or equal
        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                j = stack.pop()
                next_right_smaller = i
                if stack:
                    next_left_smaller = stack[-1]
                    L = next_right_smaller - next_left_smaller - 1
                    if nums[j] > threshold/L: 
                        res = L             
            stack.append(i)
        return res    
# @lc code=end

