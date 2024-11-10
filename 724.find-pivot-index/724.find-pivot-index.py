#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 2 * leftsum + num[i]= sums
        # leftsum == rightsum

        # at virtual index -1
        prefix_sum = 0
        sums = sum(nums)

        for i in range(len(nums)):
            if 2 * prefix_sum + nums[i] == sums:
                return i
            prefix_sum += nums[i] 
        return -1
            

        
# @lc code=end

