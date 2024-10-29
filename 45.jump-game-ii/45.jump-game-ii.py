#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jump = 0
        farthest = 0
        end = 0

        for i in range(n):
            farthest = max(farthest, i + nums[i])
            if end >= n-1:
                return jump
            if end == i:
                jump += 1
            end = farthest
        return jump
# @lc code=end

