#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count_smaller_or_equal(nums, val):
            count = 0 
            j = 1
            for i in range(len(nums)):
                #j = bisect_right(nums, val+nums[i], i+1)
                while j < len(nums) and nums[j] - nums[i] <= val:
                    j += 1
                count += j-i-1
            return count

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2 
            count = count_smaller_or_equal(nums, mid) 
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left      
# @lc code=end

