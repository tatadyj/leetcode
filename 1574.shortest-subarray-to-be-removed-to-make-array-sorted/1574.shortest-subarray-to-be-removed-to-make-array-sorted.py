#
# @lc app=leetcode id=1574 lang=python3
#
# [1574] Shortest Subarray to be Removed to Make Array Sorted
#

# @lc code=start
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        res = n - 1

        j = n - 1
        while j-1 >= 0 and arr[j-1] <= arr[j]:
            j -= 1
        res = min(res, j)
        if res == 0:
            return res

        for i in range(n):
            if i-1 >= 0 and arr[i] < arr[i-1]:
                break 
            while j < n and arr[i] > arr[j]:
                j += 1
            res = min(res, j-i-1)
        return res       
# @lc code=end

