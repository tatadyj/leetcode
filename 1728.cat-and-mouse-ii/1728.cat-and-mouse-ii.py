#
# @lc app=leetcode id=1728 lang=python3
#
# [1728] Cat and Mouse II
#

# @lc code=start
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        memo = {}
        for i in range(m):
            for j in range(n):
                memo[(i, j)] = {}
                for ii in range(m):
                    for jj in range(n):
                        memo[(i, j)][(ii, jj)] = {}
                        memo[(i, j)][(ii, jj)][1] = 0
                        memo[(i, j)][(ii, jj)][2] = 0
                        
        cat, mouse, food = None, None, None 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'C':
                    cat = (i, j)
                if grid[i][j] == 'M':
                    mouse = (i, j)
                if grid[i][j] == 'F':
                    food = (i, j)

        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '#': continue
                if grid[i][j] == 'F': continue
                memo[food][(i, j)][1] = 1 # mouse win
                memo[food][(i, j)][2] = 1 # mouse win
                memo[(i, j)][food][1] = 2 # cat win
                memo[(i, j)][food][2] = 2 # cat win

                # mouse, cat, turn
                queue.append((food, (i, j), 1)) 
                queue.append((food, (i, j), 2))
                queue.append(((i, j), food, 1))
                queue.append(((i, j), food, 2))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '#': continue
                memo[(i, j)][(i, j)][1] = 2 # cat win
                memo[(i, j)][(i, j)][2] = 2 # cat win
                queue.append(((i, j), (i, j), 1))
                queue.append(((i, j), (i, j), 2))
        
        def get_prev_state(mm, cc, tt):
            prev = []

            if tt == 1:
                for d in dir:
                    for v in range(catJump+1):
                        prev_cx = cc[0] + d[0] * v 
                        prev_cy = cc[1] + d[1] * v
                        if prev_cx < 0 or prev_cx >= m or prev_cy < 0 or prev_cy >= n: break 
                        if grid[prev_cx][prev_cy] == '#': break 
                        prev.append((mm, (prev_cx, prev_cy), 2))
            elif tt == 2:
                for d in dir:
                    for v in range(mouseJump+1):
                        prev_mx = mm[0] + d[0] * v 
                        prev_my = mm[1] + d[1] * v
                        if prev_mx < 0 or prev_mx >= m or prev_my < 0 or prev_my >= n: break 
                        if grid[prev_mx][prev_my] == '#': break 
                        prev.append(((prev_mx, prev_my), cc, 1))                

            return prev 
        
        def is_all_nxt_win(mm, cc, tt):
            if tt == 1: # 当前是老鼠轮
                for d in dir:
                    for v in range(mouseJump+1):
                        nxt_mx = mm[0] + d[0] * v 
                        nxt_my = mm[1] + d[1] * v
                        if nxt_mx < 0 or nxt_mx >= m or nxt_my < 0 or nxt_my >= n: break 
                        if grid[nxt_mx][nxt_my] == '#': break 
                        if memo[(nxt_mx, nxt_my)][cc][2] != 2:
                            return False  

            elif tt == 2:
                for d in dir:
                    for v in range(catJump+1):
                        nxt_cx = cc[0] + d[0] * v 
                        nxt_cy = cc[1] + d[1] * v
                        if nxt_cx < 0 or nxt_cx >= m or nxt_cy < 0 or nxt_cy >= n: break 
                        if grid[nxt_cx][nxt_cy] == '#': break 
                        if memo[mm][(nxt_cx, nxt_cy)][1] != 1:
                            return False
            return True 

        step = 0
        while queue: 
            step += 1
            if step > 2000: return False   
            size = len(queue)
            for _ in range(size):
                mm, cc, tt = queue.popleft()
                win = memo[mm][cc][tt]
                print(mm, cc, tt, win)
                for prev_m, prev_c, prev_t in get_prev_state(mm, cc, tt):
                    if  memo[prev_m][prev_c][prev_t] != 0: continue 

                    if prev_t == win:
                        memo[prev_m][prev_c][prev_t] = win
                        queue.append((prev_m, prev_c, prev_t))
                    elif is_all_nxt_win(prev_m, prev_c, prev_t):
                        if prev_t == 1:
                            memo[prev_m][prev_c][prev_t] = 2
                        else:
                             memo[prev_m][prev_c][prev_t] = 1
                        queue.append((prev_m, prev_c, prev_t))

        return memo[mouse][cat][1] == 1
# @lc code=end

