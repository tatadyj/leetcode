#
# @lc app=leetcode id=2422 lang=python3
#
# [2422] Merge Operations to Turn Array Into a Palindrome
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        left_sum = nums[0]
        right_sum = nums[-1]
        i = 0 
        j = len(nums) - 1
        rets = 0
        while i < j:
            if left_sum == right_sum:
                i += 1
                j -= 1
                left_sum += nums[i]
                right_sum += nums[j]
            elif left_sum < right_sum:
                i += 1
                left_sum += nums[i]
                rets += 1
            elif left_sum > right_sum:
                j -= 1
                right_sum += nums[j]
                rets += 1
        return rets
# @lc code=end

