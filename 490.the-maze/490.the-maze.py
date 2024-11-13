#
# @lc app=leetcode id=490 lang=python3
#
# [490] The Maze
#

# @lc code=start
from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = [[False]*n for _ in range(m)]
        queue = deque()
        queue.append(start)
        visited[start[0]][start[1]] = True 
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr == destination:
                    return True 
                for dir in dirs:
                    next_i, next_j = curr
                    while next_i >=0 and next_i < m and next_j >= 0 and next_j < n and maze[next_i][next_j] == 0:
                        next_i += dir[0]
                        next_j += dir[1]
                    next_i -= dir[0]
                    next_j -= dir[1]
                    if not visited[next_i][next_j]:
                        visited[next_i][next_j] = True 
                        queue.append([next_i, next_j])
        return False
                   
# @lc code=end

