#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def count_less_or_equal(val):
            count = 0
            n = len(matrix)
            i = n - 1
            j = 0 
            while i >= 0 and j < n:
                if matrix[i][j] <= val:
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            return count


        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2
            if count_less_or_equal(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left    
# @lc code=end

