#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        res = 0
        total = 0
        for r in range(n):
            freq[nums[r]] += 1
            total += nums[r]

            if r-k >= 0: 
                val = nums[r-k]
                freq[val] -= 1
                if freq[val] == 0:
                    freq.pop(val)
                total -= val

            if r+1-k >= 0:
                if len(freq) == k:
                    res = max(res, total)
        return res    
# @lc code=end

