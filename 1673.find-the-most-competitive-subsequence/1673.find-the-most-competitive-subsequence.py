#
# @lc app=leetcode id=1673 lang=python3
#
# [1673] Find the Most Competitive Subsequence
#

# @lc code=start
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        num_removed = len(nums) - k 
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i] and num_removed > 0:
                stack.pop()
                num_removed -= 1
            stack.append(i)

        for _ in range(num_removed):
            stack.pop()
            
        return [nums[i] for i in stack]        
# @lc code=end

