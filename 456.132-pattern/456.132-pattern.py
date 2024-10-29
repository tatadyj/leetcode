#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        min_val = [None] * n
        for i in range(n):
            if i == 0:
                min_val[i] = nums[i]
            else:
                min_val[i] = min(nums[i], min_val[i-1])
        
        next_val = [None] * n 
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                j = stack.pop()
                next_val[i] = j
            stack.append(i)

        for i in range(1, n):
            if next_val[i] and min_val[i] < nums[next_val[i]]:
                return True 

        return False      
# @lc code=end

