#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
from collections import defaultdict

def atMost(nums, k):
    res = 0 
    left = 0 
    window = defaultdict(int)

    for right in range(len(nums)):
        rval = nums[right]
        # update window
        window[rval] += 1

        while len(window) > k:
            lval = nums[left]
            left += 1
            # update window
            window[lval] -= 1
            if window[lval] == 0:
                window.pop(lval)

        res += right - left + 1

    return res 


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return atMost(nums, k) - atMost(nums, k-1)
        
# @lc code=end

