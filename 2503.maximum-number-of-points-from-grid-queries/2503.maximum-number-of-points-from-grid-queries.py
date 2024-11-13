#
# @lc app=leetcode id=2503 lang=python3
#
# [2503] Maximum Number of Points From Grid Queries
#

# @lc code=start
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(queries[i], i) for i in range(len(queries))]
        queries.sort()

        m = len(grid)
        n = len(grid[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pq = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        ans = [0] * len(queries)
        count = 0
        for q, idx in queries:
            while pq and pq[0][0] < q:
                v, x, y = heapq.heappop(pq)
                #if visited[x][y]: continue 
                #visited[x][y] = True 
                count += 1
                for dx, dy in dir:
                    nxt_x, nxt_y = x + dx, y + dy
                    if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n: continue 
                    if visited[nxt_x][nxt_y]: continue 
                    heapq.heappush(pq, (grid[nxt_x][nxt_y], nxt_x, nxt_y))
                    visited[nxt_x][nxt_y] = True
            ans[idx] = count
        return ans

        # 本质上是BFS 但是同一层需要排序，比如第三层【3，5，3】
        # 需要排序【3，3，5】。 3，3 可以拓展到第四层，即使5被block
        # 不能算是Dijkstra 
          
# @lc code=end

