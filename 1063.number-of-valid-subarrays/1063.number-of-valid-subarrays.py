#
# @lc app=leetcode id=1063 lang=python3
#
# [1063] Number of Valid Subarrays
#

# @lc code=start
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        next_smaller = [n] * n

        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                j = stack.pop()
                next_smaller[j] = i 
            stack.append(i)
        count = 0 
        for i,v in enumerate(next_smaller):
            count += v - i

        return count        
# @lc code=end

