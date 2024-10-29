#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List 

def templateOne(nums, target):
    # 基础模版1， 只能保证找到一个
    if len(nums) == 0:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left < right - 1:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid 
        elif target > nums[mid]:
            left = mid
        else:
            return mid

    # 终止条件 left == right - 1
    if nums[left] == target:
        return left 
    elif nums[right] == target:
        return right 
    else:
        return -1

def templateTwo(nums, target):
    # 基础模版2， 保证找到第一个
    if len(nums) == 0:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left < right - 1:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid 
        elif target > nums[mid]:
            left = mid
        else:
            right = mid # 特殊

    # 终止条件 left == right - 1
    if nums[left] == target: # 先左后右
        return left 
    elif nums[right] == target:
        return right 
    else:
        return -1

def templateThree(nums, target):
    # 基础模版3， 保证找到最后一个
    if len(nums) == 0:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left < right - 1:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid 
        elif target > nums[mid]:
            left = mid
        else:
            left = mid # 特殊

    # 终止条件 left == right - 1
    if nums[right] == target: # 先右后左
        return right 
    elif nums[left] == target:
        return left 
    else:
        return -1

def templateFour(nums, target):
    # 基础模版4， 找到最接近的
    if len(nums) == 0:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left < right - 1:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid 
        elif target > nums[mid]:
            left = mid
        else:
            return mid

    # 终止条件 left == right - 1
    return left if target - nums[left] <= nums[right] - target else right 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return templateOne(nums, target)

print(Solution().search([3,3,3,3,3,5], 4))
# @lc code=end

