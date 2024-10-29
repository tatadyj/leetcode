#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#

# @lc code=start
from typing import List

def bt(ans, subseq, nums):
    if len(subseq) >= 2:
        ans.append(subseq[:])

    used = set()
    for i in range(len(nums)):
        if nums[i] in used:
            continue
        if len(subseq) != 0 and nums[i] < subseq[-1]:
            continue
        else:
            used.add(nums[i])
            subseq.append(nums[i])
            bt(ans, subseq, nums[i+1:])
            subseq.pop()

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans, subseq = [], []
        bt(ans, subseq, nums)
        return ans


print(Solution().findSubsequences([4,7,6,7]))
# @lc code=end

