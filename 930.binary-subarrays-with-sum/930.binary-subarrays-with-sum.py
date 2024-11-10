#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(goal):
            if goal < 0:
                return 0 
                
            sum = 0
            left = 0 
            count = 0
            for right in range(len(nums)):
                rval = nums[right]
                sum += rval 

                while left < len(nums) and sum > goal:
                    lval = nums[left]
                    sum -= lval 
                    left += 1
                
                count += right - left + 1
            return count
        #print(at_most(goal), at_most(goal-1))
        return at_most(goal) - at_most(goal-1)


        
# @lc code=end

