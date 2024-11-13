#
# @lc app=leetcode id=499 lang=python3
#
# [499] The Maze III
#

# @lc code=start
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        visited = [[False]*n for _ in range(m)]
        ball = tuple(ball)
        hole = tuple(hole)
        pq = [(0, '', ball[0], ball[1])]
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        name = ['u', 'd', 'l', 'r']

        while pq:
            d, s, i, j = heapq.heappop(pq)
            #print(i, j, s)
            if visited[i][j]: continue 
            visited[i][j] = True 
            if (i, j) == hole:
                return s
            for k, dir in enumerate(dirs):
                next_i, next_j = i, j
                next_d = d
                next_s = s
                while next_i >=0 and next_i < m and next_j >= 0 and next_j < n and maze[next_i][next_j] == 0 and (next_i, next_j) != hole:
                    next_i += dir[0]
                    next_j += dir[1]
                    next_d += 1
                if (next_i, next_j) == hole:
                    next_s += name[k]   
                else:  
                    next_i -= dir[0]
                    next_j -= dir[1]
                    next_d -= 1
                    if next_d != d:
                        next_s += name[k]                    
                if visited[next_i][next_j]: continue 
                heapq.heappush(pq, (next_d, next_s, next_i, next_j))
        return 'impossible'
       
                               
# @lc code=end

