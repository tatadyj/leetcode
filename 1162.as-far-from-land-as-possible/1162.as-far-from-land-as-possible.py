#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#

# @lc code=start
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dist = [[-1]*n for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    dist[i][j] = 0 

        if not queue: return -1
        if len(queue) == n*n: return -1
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_i, curr_j, level = queue.popleft()
                for di, dj in dir:
                    nxt_i, nxt_j = curr_i + di, curr_j + dj
                    if nxt_i < 0 or nxt_i >= n or nxt_j < 0 or nxt_j >= n: continue 
                    if dist[nxt_i][nxt_j] != -1: continue
                    queue.append((nxt_i, nxt_j, level+1))
                    dist[nxt_i][nxt_j] = level + 1
        max_dist = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    max_dist = max(max_dist, dist[i][j])
        return max_dist
                    
        

          
# @lc code=end

