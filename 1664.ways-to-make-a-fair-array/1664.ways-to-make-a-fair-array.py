#
# @lc app=leetcode id=1664 lang=python3
#
# [1664] Ways to Make a Fair Array
#

# @lc code=start
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums) 
        prefix_odd = [0] * (n+1)
        prefix_even = [0] * (n+1)

        for i in range(n):
            if i % 2 == 1:
                prefix_odd[i+1] = prefix_odd[i] + nums[i]
                prefix_even[i+1] = prefix_even[i]
            else:
                prefix_even[i+1] = prefix_even[i] + nums[i]
                prefix_odd[i+1] = prefix_odd[i]

        ret = 0
        suffix_odd, suffix_even = 0, 0
        for j in range(n-1, -1, -1):
            if prefix_odd[j] + suffix_even == prefix_even[j] + suffix_odd:
                ret += 1
            if j % 2 == 1:
                suffix_odd += nums[j]
            else:
                suffix_even += nums[j]
        return ret   
# @lc code=end

