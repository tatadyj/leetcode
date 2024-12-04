#
# @lc app=leetcode id=913 lang=python3
#
# [913] Cat and Mouse
#

# @lc code=start
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        memo = {}
        for i in range(n):
            memo[i] = {}
            for j in range(1, n):
                memo[i][j] = {}
                memo[i][j][1] = 0
                memo[i][j][2] = 0

        queue = deque()
        for i in range(1, n):
            memo[0][i][1] = 1 # mouse win
            memo[0][i][2] = 1 # mouse win 
            memo[i][i][1] = 2 # cat win
            memo[i][i][2] = 2 # cat win
            queue.append((0, i, 1))
            queue.append((0, i, 2))
            queue.append((i, i, 1))
            queue.append((i, i, 2))

        def get_prev_state(mm, cc, tt):
            prev = []
            if tt == 1:
                for prev_c in graph[cc]:
                    if prev_c == 0: continue 
                    prev.append((mm, prev_c, 2))
            elif tt == 2:
                for prev_m in graph[mm]:
                    prev.append((prev_m, cc, 1))
            return prev

        def is_all_nxt_win(mm, cc, tt):
            if tt == 1:
                for nxt_m in graph[mm]:
                    if memo[nxt_m][cc][2] != 2:
                        return False 
            
            elif tt == 2:
                for nxt_c in graph[cc]:
                    if nxt_c == 0: continue 
                    if memo[mm][nxt_c][1] != 1:
                        return False

            return True


        while queue:
            mm, cc, tt = queue.popleft()
            win = memo[mm][cc][tt]
            for prev_m, prev_c, prev_t in get_prev_state(mm, cc, tt):
                if memo[prev_m][prev_c][prev_t] != 0: continue 

                if win == prev_t:
                    memo[prev_m][prev_c][prev_t] = win
                    queue.append((prev_m, prev_c, prev_t))

                elif is_all_nxt_win(prev_m, prev_c, prev_t):
                    if prev_t == 1:
                        memo[prev_m][prev_c][prev_t] = 2
                    else:
                        memo[prev_m][prev_c][prev_t] = 1
                    queue.append((prev_m, prev_c, prev_t))

        return memo[1][2][1]
    
              
# @lc code=end

