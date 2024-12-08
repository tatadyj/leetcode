#
# @lc app=leetcode id=491 lang=python3
#
# [491] Non-decreasing Subsequences
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def bt(curr):
            if len(path) >= 2:
                ans.append(path[:])

            used = set()
            for i in range(curr, len(nums)):
                if nums[i] in used: continue
                if path and path[-1] > nums[i]: continue 
                path.append(nums[i])
                used.add(nums[i])
                bt(i+1)
                path.pop()

        ans, path = [], []
        bt(0)
        return ans
          
# @lc code=end

