#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        smallest_diff = float('inf')
        res = None
        nums.sort()
        n = len(nums)
        for i in range(n):
            left = i + 1 
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    if smallest_diff > abs(total - target):
                        res = total 
                        smallest_diff = abs(total - target)
                    left += 1 
                elif total > target:
                        if smallest_diff > abs(total - target):
                            res = total 
                            smallest_diff = abs(total - target)                 
                        right -= 1 
                else:
                    return total 
        return res 
# @lc code=end

