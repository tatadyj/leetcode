#
# @lc app=leetcode id=1263 lang=python3
#
# [1263] Minimum Moves to Move a Box to Their Target Location
#

# @lc code=start
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo0 = [[-1] * n for _ in range(m)]
        memo = [[deepcopy(memo0) for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    px, py = i, j 
                    grid[i][j] = '.'
                if grid[i][j] == 'B':
                    bx, by = i, j 
                    grid[i][j] = '.'
                if grid[i][j] == 'T':
                    tx, ty = i, j 
                    grid[i][j] = '.'

        dq = deque() 
        dq.append((bx, by, px, py, 0))
        memo[bx][by][px][py] = 0
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while dq:
            size = len(dq)
            for _ in range(size):
                bx, by, px, py, lvl = dq.popleft()
                if bx == tx and by == ty:
                    return memo[bx][by][px][py]
                for dx, dy in dir:
                    nxt_px, nxt_py = px + dx, py + dy
                    if nxt_px < 0 or nxt_px >= m or nxt_py < 0 or nxt_py >= n: continue 
                    if grid[nxt_px][nxt_py] != '.': continue 
                    if nxt_px == bx and nxt_py == by: continue # block by box
                    if memo[bx][by][nxt_px][nxt_py] >= 0: continue
                    memo[bx][by][nxt_px][nxt_py] = memo[bx][by][px][py]
                    dq.appendleft((bx, by, nxt_px, nxt_py, lvl))
                
                if abs(px - bx) + abs(py - by) == 1:
                    for dx, dy in dir:
                        if px + dx == bx and py + dy == by: # same direction as box
                            nxt_bx = bx + dx
                            nxt_by = by + dy
                            if nxt_bx < 0 or nxt_bx >= m or nxt_by < 0 or nxt_by >= n: continue 
                            if grid[nxt_bx][nxt_by] != '.': continue 
                            if memo[nxt_bx][nxt_by][bx][by] >= 0: continue
                            memo[nxt_bx][nxt_by][bx][by] = memo[bx][by][px][py] + 1
                            dq.append((nxt_bx, nxt_by, bx, by, lvl+1))
        return -1
# @lc code=end

