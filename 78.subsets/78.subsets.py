#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List
def bt(ans, subset, nums):
    ans.append(subset[:])

    for i in range(len(nums)):
            subset.append(nums[i])
            bt(ans, subset, nums[i+1:])
            subset.pop()

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, subset = [], []
        bt(ans, subset, nums)
        return ans


s = Solution()
print(s.subsets([1,2,3]))
# @lc code=end

