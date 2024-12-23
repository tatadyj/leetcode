#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for k in range(n):
            if target <= 0 and nums[k] > 0:
                break 
            if k > 0 and nums[k] == nums[k-1]:
                continue
            for i in range(k + 1, n):
                if target <= 0 and nums[k] + nums[i] > 0:
                    break
                if i > k+1 and nums[i] == nums[i-1]:
                    continue  
                left = i + 1 
                right = n - 1 
                while left < right:
                    total = nums[k] + nums[i] + nums[left] + nums[right]
                    if total < target:
                        left += 1 
                    elif total > target:
                        right -= 1 
                    else:
                        res.append([nums[k], nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]: left += 1
                        while left < right and nums[right] == nums[right - 1]: right -= 1
                        left += 1
                        right -= 1
        return res
        # @lc code=end

