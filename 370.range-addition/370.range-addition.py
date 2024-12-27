#
# @lc app=leetcode id=370 lang=python3
#
# [370] Range Addition
#

# @lc code=start
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * length
        for update in updates:
            start, end, val = update
            arr[start] += val 
            if end + 1 < length:
                arr[end + 1] -= val

        for i in range(1, length):
            arr[i] = arr[i] + arr[i-1]

        return arr  
# @lc code=end

