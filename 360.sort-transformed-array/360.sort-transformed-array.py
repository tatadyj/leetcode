#
# @lc app=leetcode id=360 lang=python3
#
# [360] Sort Transformed Array
#

# @lc code=start
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = []

        if a == 0:
            for num in nums:
                res.append(b*num + c)
            if b < 0:
                res = res[::-1] 
        else:
            # f' = 0
            # 2ax + b = 0
            # x = -b/2/a
            mid = -b/2/a 
            left = 0 
            right = len(nums) - 1
            while left <= right:
                if abs(mid - nums[left]) > abs(mid - nums[right]):
                    res.append(a*nums[left]*nums[left] + b*nums[left] + c)
                    left += 1
                else:
                    res.append(a*nums[right]*nums[right] + b*nums[right] + c)
                    right -= 1

            if a > 0:
                res = res[::-1]
        return res 

                  
# @lc code=end

