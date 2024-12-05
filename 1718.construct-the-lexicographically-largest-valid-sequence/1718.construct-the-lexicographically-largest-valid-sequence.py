#
# @lc app=leetcode id=1718 lang=python3
#
# [1718] Construct the Lexicographically Largest Valid Sequence
#

# @lc code=start
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        used = [False] * (n + 1)
        ans = [None] * (2*n - 1)
        
        def dfs(pos):
            if pos == 2*n - 1:
                return True 

            if ans[pos]:
                return dfs(pos + 1)

            for d in range(n, 0, -1):
                if used[d]: continue 
                if d > 1 and (pos + d >= 2*n-1 or ans[pos + d]): continue 
                used[d] = True 
                ans[pos] = d 
                if d > 1:
                    ans[pos + d] = d 

                if dfs(pos + 1):
                    return True 

                used[d] = False 
                ans[pos] = None 
                if d > 1:
                    ans[pos + d] = None 
            return False 

        dfs(0)
        return ans  
# @lc code=end

