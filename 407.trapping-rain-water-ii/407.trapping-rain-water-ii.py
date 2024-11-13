#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#

# @lc code=start
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pq = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    pq.append((heightMap[i][j], i, j))
        heapq.heapify(pq)
        visited = [[False] * n for _ in range(m)]

        ret = 0
        curr = -inf
        while pq:
            h, x, y = heapq.heappop(pq)
            if visited[x][y]: continue
            visited[x][y] = True
            if curr < h:
                curr = h 
            ret += curr - h
            for dx, dy in dir:
                nxt_x, nxt_y = x + dx, y + dy
                if nxt_x < 0 or nxt_x >= m or nxt_y < 0 or nxt_y >= n: continue 
                if visited[nxt_x][nxt_y]: continue 
                heapq.heappush(pq, (heightMap[nxt_x][nxt_y], nxt_x, nxt_y))
        return ret   
# @lc code=end

