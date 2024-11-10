#
# @lc app=leetcode id=1477 lang=python3
#
# [1477] Find Two Non-overlapping Sub-arrays Each With Target Sum
#

# @lc code=start
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        res = float('inf')
        minBefore = [float('inf')]*len(arr)
        window_sum = 0 
        left, right = 0, 0 
        while right < len(arr):
            rval = arr[right]
            right += 1 
            # update window 
            window_sum += rval 

            if window_sum == target:
                res = min(res, minBefore[left-1] + right - left)
                minBefore[right-1] = min(minBefore[right-2], right-left)
            if window_sum < target:
                minBefore[right-1] = minBefore[right - 2]

            while window_sum > target:
                lval = arr[left]
                left += 1 
                # update window
                window_sum -= lval 

 
        return res if minBefore[right-1] != float('inf') else -1 

Solution().minSumOfLengths([3,2,2,4,3],3)
# @lc code=end

