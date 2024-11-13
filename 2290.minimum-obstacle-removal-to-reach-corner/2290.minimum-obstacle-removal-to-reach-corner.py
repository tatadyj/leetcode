#
# @lc app=leetcode id=2290 lang=python3
#
# [2290] Minimum Obstacle Removal to Reach Corner
#

# @lc code=start
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False]*n for _ in range(m)]
        visited[0][0]= True
        queue = deque()
        queue.append((0, 0, 0)) # i, j,level
        
        def travel(i, j):
            q = deque()
            q.append((i, j))
            visited[i][j] = True 
            ret = []
            while q:
                x, y = q.popleft()
                for dx, dy in dir:
                    nxt_x, nxt_y = x + dx, y + dy
                    if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n: continue
                    if visited[nxt_x][nxt_y]: continue
                    visited[nxt_x][nxt_y]= True
                    if nxt_x == m-1 and nxt_y == n-1:
                        return [(nxt_x, nxt_y)]
                    if grid[nxt_x][nxt_y] == 0:
                        q.append((nxt_x, nxt_y)) 
                    else:
                        ret.append((nxt_x, nxt_y))
            return ret 


        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, l = queue.popleft()
                for dx, dy in dir:
                    nxt_x, nxt_y = x + dx, y + dy
                    if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n: continue
                    if visited[nxt_x][nxt_y]: continue
                    if nxt_x == m-1 and nxt_y == n-1:
                        return l 
                    if grid[nxt_x][nxt_y] == 1:
                        queue.append((nxt_x, nxt_y, l+1))
                        visited[nxt_x][nxt_y]= True
                    else:
                        for nxt_i, nxt_j in travel(nxt_x, nxt_y):
                            if nxt_i == m-1 and nxt_j == n-1:
                                return l 
                            queue.append((nxt_i, nxt_j, l+1))                 
        return -1
        
# @lc code=end

