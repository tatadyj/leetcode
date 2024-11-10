#
# @lc app=leetcode id=1546 lang=python3
#
# [1546] Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
#

# @lc code=start
from collections import defaultdict

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        hash = defaultdict(int)
        res = 0
        prefix_sum = 0 
        frontier = -1

        hash[prefix_sum] = -1
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - target in hash and hash[prefix_sum-target] >= frontier:
                res += 1 
                frontier = i 
            hash[prefix_sum] = i
        return res 
# @lc code=end

