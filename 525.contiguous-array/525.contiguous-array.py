#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        # 0 -> - 1
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1 
        
        # prefix sum
        hash = {} # key: prefix_sum, value: index 
        prefix_sum = 0
        hash[prefix_sum] = -1
        for i in range(len(nums)):
            # 更新 prefix_sum
            prefix_sum += nums[i]
            if prefix_sum in hash:
                res = max(res, i-hash[prefix_sum])
            
            if prefix_sum not in hash:
                hash[prefix_sum] = i  # 记录第一次出现的引索
         

        return res 
# @lc code=end

