#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#

# @lc code=start
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            while j >= i and nums[i] + nums[j] > target:
                j -= 1
            if j < i: break 
            res += 2**(j-i) # 固定i多少个j， j-i个
        return res % (10**9 + 7)
# @lc code=end

