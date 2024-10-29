#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_hash = defaultdict(int) # key is sum, value is cnt
        prefix_hash[0] = 1
        prefix_sum = 0
        
        res = 0
        for n in nums:
            prefix_sum += n
            if prefix_sum - k in prefix_hash:
                res += prefix_hash[prefix_sum - k]
            prefix_hash[prefix_sum] += 1
        return res
# @lc code=end

