#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
def cleanCode(nums, target):
        dict = {}
        for i,n in enumerate(nums):
            if target - n not in dict:
                dict[n] = i
            else:
                return [i, dict[target - n]] 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            dict[num] = i

        for i, num in enumerate(nums):
            if target - num in dict and dict[target - num] != i:
                return [i, dict[target - num]]

        return []
        
# @lc code=end

