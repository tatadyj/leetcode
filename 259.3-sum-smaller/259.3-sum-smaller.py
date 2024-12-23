#
# @lc app=leetcode id=259 lang=python3
#
# [259] 3Sum Smaller
#

# @lc code=start
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0 
        for i in range(n):
            left = i+1
            right = n-1 
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    #print(total)
                    res += right - left
                    left += 1
                else:
                    right -= 1
        
        return res 
# @lc code=end

