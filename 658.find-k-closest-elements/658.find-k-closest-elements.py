#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
def binarySearch(arr, x):
    l, r = 0, len(arr)-1
    while l < r - 1:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid 
        elif arr[mid] > x:
            r = mid 
        else:
            return mid 
    
    return l if abs(arr[l] - x) < abs(arr[r] - x) else r 

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = binarySearch(arr, x)
        ans = []
        for i in range(1, k):
            left = abs(arr[idx + i] - x)
            right = abs(arr[idx - i] - x) 
            if left <

        
# @lc code=end

