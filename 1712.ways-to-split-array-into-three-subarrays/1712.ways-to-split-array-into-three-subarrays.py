#
# @lc app=leetcode id=1712 lang=python3
#
# [1712] Ways to Split Array Into Three Subarrays
#

# @lc code=start
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        res = 0
        j = 1
        for i in range(1, len(prefix_sum)):
            left = prefix_sum[i] - prefix_sum[0]
            while j <= i:
                j += 1
            while j < len(prefix_sum) and prefix_sum[j] - prefix_sum[i] < left:
                j += 1
            
            if j == len(prefix_sum):
                break

            # <= 
            k = bisect.bisect_right(prefix_sum, 0.5 * (prefix_sum[len(prefix_sum) - 1] + prefix_sum[i])) - 1 
            if k == len(prefix_sum) - 1:
                k -= 1               
            res += max(0, k - j + 1)
            if k == len(prefix_sum) - 1:
                break

        return res % (10**9 + 7)

# @lc code=end

