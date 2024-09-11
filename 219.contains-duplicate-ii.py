#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        left, right = 0, 1

        while right < len(nums):
            right += 1
            if nums[left] == nums[right-1]:
                return True 

            print(f"windows: [{left}, {right})\n")
            while right - left == k+1: 
                if nums[left] == nums[right-1]:
                    return True
                left += 1
        
        return False 
# @lc code=end

