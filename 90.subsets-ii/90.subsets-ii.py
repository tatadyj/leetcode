#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
from typing import List

def bt(ans, subset, nums):
    ans.append(subset[:])

    for i in range(len(nums)):
        if i-1 >= 0  and nums[i] == nums[i-1]:
            continue
        else:
            subset.append(nums[i])
            bt(ans, subset, nums[i+1:])
            subset.pop()

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans, subset = [], []
        nums.sort()
        bt(ans, subset, nums)
        return ans
        
s = Solution()
print(s.subsetsWithDup([1,2,2]))
# @lc code=end

