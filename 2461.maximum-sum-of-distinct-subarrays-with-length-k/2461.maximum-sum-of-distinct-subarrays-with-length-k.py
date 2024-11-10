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
        left = 0 
        total = 0
        for right in range(n):
            rval = nums[right]
            freq[rval] += 1
            total += rval 

            while right - left + 1 > k:
                lval = nums[left]
                freq[lval] -= 1
                if freq[lval] == 0:
                    freq.pop(lval)
                total -= lval
                left += 1

            if len(freq) == k:
                res = max(res, total)
        return res      
# @lc code=end

