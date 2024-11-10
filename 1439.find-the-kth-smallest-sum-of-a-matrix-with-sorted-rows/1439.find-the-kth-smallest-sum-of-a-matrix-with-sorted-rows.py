#
# @lc app=leetcode id=1439 lang=python3
#
# [1439] Find the Kth Smallest Sum of a Matrix With Sorted Rows
#

# @lc code=start
def is_ok(mat, k, val): # >= k
    m, n = len(mat), len(mat[0])
    count = 1
    total = sum([mat[i][0] for i in range(m)])
    if total > val:
        return False 

    def dfs(ans, r, sum_val, k, val):
        if ans[0] >= k:
            return 
        
        if r == m:
            return 

        for c in range(n):
            if sum_val - mat[r][0] + mat[r][c] <= val:
                if c > 0: ans[0] += 1
                dfs(ans, r+1, sum_val - mat[r][0] + mat[r][c], k, val) 
    
    ans = [count]
    dfs(ans, 0, total, k, val)
    return ans[0] >= k

   

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        
        left = sum([n[0] for n in mat])
        right = sum([n[-1] for n in mat])

        while left < right:
            mid = (left + right) // 2
            if is_ok(mat, k, mid):
                right = mid
            else:
                left = mid + 1 
        return left 
        
        # pq 解法
         
        
# @lc code=end

