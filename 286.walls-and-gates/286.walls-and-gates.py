#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

# @lc code=start
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False]*n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j, 0))
                    visited[i][j] = True 

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, l = queue.popleft()
                for dx, dy in dir:
                    nxt_x, nxt_y = x + dx, y + dy
                    if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n: continue 
                    if visited[nxt_x][nxt_y]: continue 
                    if rooms[nxt_x][nxt_y] == -1: continue 
                    rooms[nxt_x][nxt_y] = l + 1
                    queue.append((nxt_x, nxt_y, l+1))
                    visited[nxt_x][nxt_y] = True 

# @lc code=end

