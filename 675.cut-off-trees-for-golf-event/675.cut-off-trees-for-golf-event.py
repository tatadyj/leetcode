#
# @lc app=leetcode id=675 lang=python3
#
# [675] Cut Off Trees for Golf Event
#

# @lc code=start
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        map = {}
        m = len(forest)
        n = len(forest[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if forest[i][j] == 0: continue 
                if forest[i][j] == 1: continue
                map[forest[i][j]] = (i, j)
        
        def bfs(start, end):
            if start == end:
                return 0

            queue = deque()
            queue.append((start[0], start[1], 0))
            visited = [[False] * n for _ in range(m)]
            visited[start[0]][start[1]] = True 
            while queue:
                size = len(queue)
                for _ in range(size):
                    x, y, l = queue.popleft()
                    for dx, dy in dir:
                        nxt_x, nxt_y = x + dx, y + dy 
                        if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n: continue 
                        if visited[nxt_x][nxt_y]: continue 
                        if forest[nxt_x][nxt_y] == 0: continue
                        if nxt_x == end[0] and nxt_y == end[1]:
                            return l + 1 
                        queue.append((nxt_x, nxt_y, l+1))
                        visited[nxt_x][nxt_y] = True 
            return -1

        ans = 0
        start = (0, 0)
        for v in sorted(map):
            end = map[v]
            ret = bfs(start, end)
            #print(v, ret)
            if ret == -1:
                return -1 
            ans += ret
            start = end
        return ans
           
# @lc code=end

