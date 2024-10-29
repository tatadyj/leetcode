#
# @lc app=leetcode id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_idx = max_idx = bad_idx = -1 
        res = 0 
        for i,n in enumerate(nums):
            if n > maxK or n < minK:
                bad_idx = i 

            if n == maxK:
                max_idx = i 

            if n == minK:
                min_idx = i 

            start = min(min_idx, max_idx)
            if start > bad_idx:
                res += start - (bad_idx + 1) + 1

        return res 
        
# @lc code=end

