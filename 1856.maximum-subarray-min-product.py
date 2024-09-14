#
# @lc app=leetcode id=1856 lang=python3
#
# [1856] Maximum Subarray Min-Product
#

# @lc code=start
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        next_smaller = [n] * n
        prev_smaller = [-1] * n 

        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                j = stack.pop()
                next_smaller[j] = i 
            stack.append(i)

        stack.clear() 

        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                j = stack.pop()
                prev_smaller[j] = i
            stack.append(i)

        prefix_sum = [0] + nums
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]

        res = 0
        for i in range(n):
            left = prev_smaller[i]
            right = next_smaller[i]
            val = nums[i] * (prefix_sum[right] - prefix_sum[left+1])
            res = max(res, val)
        return res % (10**9 + 7)
            
# @lc code=end

