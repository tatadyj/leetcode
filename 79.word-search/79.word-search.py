#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        #if len(word) > m*n:
        #    return False 


        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y, w):
            for dx, dy in dir:
                nxt_x, nxt_y = x + dx, y + dy
                if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n: continue 
                if visited[nxt_x][nxt_y]: continue 
                if board[nxt_x][nxt_y] != word[w+1]: continue 
                if w+1 == len(word)-1:
                    return True 
                visited[nxt_x][nxt_y] = True 
                if dfs(nxt_x, nxt_y, w+1):
                    return True 
                visited[nxt_x][nxt_y] = False
            return False 

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True 
                    visited = [[False]* n for _ in range(m)]
                    visited[i][j] = True
                    if dfs(i, j, 0):
                        return True 
        return False   
# @lc code=end

