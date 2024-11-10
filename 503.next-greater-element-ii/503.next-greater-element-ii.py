#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
from typing import List 

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = [0]

        for i in range(1, len(nums)*2):
            # 只需要定义i_mod代替i，其他都不变
            i_mod = i % len(nums)
            if nums[i_mod] <= nums[stack[-1]]:
                stack.append(i_mod)
            else:
                while stack and nums[i_mod] > nums[stack[-1]]:
                    j = stack.pop()
                    res[j] = nums[i_mod]
                stack.append(i_mod)

        return res 
        

Solution().nextGreaterElements([1,2,1])
# @lc code=end

