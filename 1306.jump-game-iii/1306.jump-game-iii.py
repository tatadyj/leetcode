#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

# @lc code=start

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()    

        def dfs(idx):
            if arr[idx] == 0:
                return True

            for next_idx in [idx + arr[idx], idx - arr[idx]]:
                if next_idx < 0 or next_idx >= len(arr): continue 
                if next_idx in visited: continue 
                visited.add(next_idx)
                if dfs(next_idx):
                    return True 
            return False
                
        return dfs(start)
   
# @lc code=end

