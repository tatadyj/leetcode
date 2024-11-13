#
# @lc app=leetcode id=1102 lang=python3
#
# [1102] Path With Maximum Minimum Value
#

# @lc code=start
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        def is_ok(score):
            if grid[0][0] < score:
                return False 
            
            queue = deque()
            queue.append((0,0))
            visited = [[False]*n for _ in range(m)]
            visited[0][0] = True 
            while queue:
                x, y = queue.popleft()
                for dx, dy in dir:
                    nxt_x, nxt_y = x + dx, y + dy
                    if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n: continue 
                    if grid[nxt_x][nxt_y] < score: continue 
                    if visited[nxt_x][nxt_y]: continue 
                    if nxt_x == m-1 and nxt_y == n-1:
                        return True 
                    queue.append((nxt_x, nxt_y))
                    visited[nxt_x][nxt_y] = True 
            return False

        m = len(grid)
        n = len(grid[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        left = 0 
        right = 10**9
        while left < right:
            mid = (left + right + 1) // 2
            if is_ok(mid):
                left = mid 
            else:
                right = mid - 1
        return left 
# @lc code=end

