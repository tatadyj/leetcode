#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        n = len(arr)
        left, right = 0, n - 1
        while left + 1 < n and arr[left] < arr[left + 1]: left += 1
        while right - 1 >= 0 and arr[right] < arr[right - 1]: right -= 1

        if left == right and left != 0 and right != n - 1: 
            return True
        else:
            return False
        
# @lc code=end

