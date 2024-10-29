#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # hint (prefix_sum1 - prefix_sum2) % k == 0 
        # -> prefix_sum1 % k == prefix_sum2 % k
        hash = defaultdict(int)
        prefix_sum = 0

        hash[prefix_sum] = -1
        for i in range(len(nums)):
            prefix_sum += nums[i]
            prefix_sum = prefix_sum % k
            
            if prefix_sum not in hash:
                hash[prefix_sum] = i 

            if prefix_sum in hash and i - hash[prefix_sum] >=2:
                return True 
            
        
        return False 




        
# @lc code=end

