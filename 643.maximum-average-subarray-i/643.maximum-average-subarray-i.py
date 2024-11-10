#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start


from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[0:k])
        res = total

        for i in range(k, len(nums)):
            total += nums[i] - nums[i-k]
            res = max(res, total)
        return res / k

Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4)
# @lc code=end

