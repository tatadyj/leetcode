#
# @lc app=leetcode id=1292 lang=python3
#
# [1292] Maximum Side Length of a Square with Sum Less than or Equal to Threshold
#

# @lc code=start
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        prefix_sum =[[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + mat[i-1][j-1]

        def is_valid(val):
            for btm_i in range(val, m+1):
                for btm_j in range(val, n+1):
                    top_i, top_j = btm_i - val, btm_j - val
                    area = prefix_sum[btm_i][btm_j] - prefix_sum[btm_i][top_j] - prefix_sum[top_i][btm_j] + prefix_sum[top_i][top_j]
                    if area <= threshold:
                        return True 
            return False 
                    


        left = 0 
        right = min(m, n)
        while left < right:
            mid = (left + right + 1) // 2
            if is_valid(mid):
                left = mid 
            else:
                right = mid - 1
        return left
        
# @lc code=end

