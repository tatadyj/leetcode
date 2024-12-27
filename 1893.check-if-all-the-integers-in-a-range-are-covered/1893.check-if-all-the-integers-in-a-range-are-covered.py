#
# @lc app=leetcode id=1893 lang=python3
#
# [1893] Check if All the Integers in a Range Are Covered
#

# @lc code=start
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52  

        for start, end in ranges:
            diff[start] += 1 
            diff[end+1] -= 1

        sum = 0 
        for i in range(1, len(diff)-1):
            sum += diff[i]
            if i >= left and i <= right and sum < 1: # 考察每个在[left, right]之间的i
                return False 
        return True   
# @lc code=end

