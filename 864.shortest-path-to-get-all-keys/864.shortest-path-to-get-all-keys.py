#
# @lc app=leetcode id=864 lang=python3
#
# [864] Shortest Path to Get All Keys
#

# @lc code=start
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        queue = deque() # (i, j, state, level), state is bitmask of number of keys
        m = len(grid)
        n = len(grid[0])
        visited = [[set() for _ in range(n)] for _ in range(m)]
        key = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@': 
                    queue.append((i, j, 0, 0))
                    visited[i][j].add(0)
                elif grid[i][j] in 'abcdef':
                    key += 1
        
        target_state = 0
        for i in range(key):
            target_state = target_state | (1 << i)
        
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, state, level = queue.popleft()
                for dx, dy in d:
                    new_x, new_y = x + dx, y + dy
                    new_state = state
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n: continue 
                    if grid[new_x][new_y] == '#': continue
                    if grid[new_x][new_y] in 'ABCDEF' and (state >> ord(grid[new_x][new_y]) - ord('A')) & 1 == 0: continue 
                    if grid[new_x][new_y] in 'abcdef':
                        new_state = state | (1 << ord(grid[new_x][new_y]) - ord('a'))
                    if new_state in visited[new_x][new_y]: continue    
                    if new_state == target_state:
                        return level + 1
                    queue.append((new_x, new_y, new_state, level + 1))
                    visited[new_x][new_y].add(new_state)
        return -1    
# @lc code=end

