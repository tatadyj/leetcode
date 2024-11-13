#
# @lc app=leetcode id=505 lang=python3
#
# [505] The Maze II
#

# @lc code=start
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        visited = [[False]*n for _ in range(m)]
        start = tuple(start)
        destination = tuple(destination)
        pq = [(0, start[0], start[1])]
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while pq:
            d, i, j = heapq.heappop(pq)
            if visited[i][j]: continue 
            visited[i][j] = True 
            if (i, j) == destination:
                return d
            for dir in dirs:
                next_i, next_j = i, j
                next_d = d
                while next_i >=0 and next_i < m and next_j >= 0 and next_j < n and maze[next_i][next_j] == 0:
                    next_i += dir[0]
                    next_j += dir[1]
                    next_d += 1
                next_i -= dir[0]
                next_j -= dir[1]
                next_d -= 1
                if visited[next_i][next_j]: continue 
                heapq.heappush(pq, (next_d, next_i, next_j))
        return -1
                    
# @lc code=end

