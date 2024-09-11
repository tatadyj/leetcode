#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m*n-1

        while l < r - 1:
            mid = (l + r) // 2
            row = mid // n 
            col = mid % n 
            if matrix[row][col] < target:
                l = mid 
            elif matrix[row][col] > target:
                r = mid 
            else:
                return True 

        lrow, lcol = l // n, l % n
        rrow, rcol = r // n, r % n 

        return matrix[lrow][lcol] == target or matrix[rrow][rcol] == target

        
# @lc code=end

