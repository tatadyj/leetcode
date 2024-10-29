#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
from typing import List 

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0 
        res = 0
        product = 1
        for right in range(len(nums)):
            rval = nums[right]
            # update window 
            product *= rval
           
            print(f"window: [{left}, {right})\n")
            # reduce window
            while product >= k:
                lval = nums[left]
                left += 1 
                # update window
                product /= lval 
            # 难点：以右边为端点的subarray个数 = subarray 长度
            # eg. [10, 2, 5]-> [5], [2, 5], [10, 2, 5]
            res += right - left + 1
        return res 

print(Solution().numSubarrayProductLessThanK([10,5,2,6],100))


# @lc code=end

