#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#

# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        res = 0
        max_freq = 0
        left = 0 
        for right in range(len(nums)):
            rval = nums[right]
            window[rval] += 1
            while window[rval] > k:
                lval = nums[left]
                window[lval] -= 1
                if window[lval] == 0:
                    window.pop(lval)
                left += 1
            res = max(res, right - left + 1)
        return res 
    
# @lc code=end

