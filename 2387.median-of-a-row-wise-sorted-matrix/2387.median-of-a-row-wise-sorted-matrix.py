#
# @lc app=leetcode id=2387 lang=python3
#
# [2387] Median of a Row Wise Sorted Matrix
#

# @lc code=start
class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def count_less_or_equal(val):
            count = 0 
            for i in range(m):
                count += bisect.bisect_right(grid[i], val) - 1 - 0 + 1
            return count

        left = min([x[0] for x in grid])
        right = max([x[-1] for x in grid])
        while left < right:
            mid = (left + right) // 2
            if count_less_or_equal(mid) >= (m*n)//2+1:
                right = mid
            else:
                left = mid + 1
        return left 
    
# @lc code=end

