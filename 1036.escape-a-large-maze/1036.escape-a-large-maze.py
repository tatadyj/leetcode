#
# @lc app=leetcode id=1036 lang=python3
#
# [1036] Escape a Large Maze
#

# @lc code=start
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set([tuple(item) for item in blocked])

        def bfs(start, end):
            queue = deque()
            queue.append(start)
            visited = set()
            visited.add(start)
            dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while queue and len(visited) <= 19900:
                x, y = queue.popleft()
                for dx, dy in dir:
                    nxt_x, nxt_y = x + dx, y + dy
                    if nxt_x < 0 or nxt_x >= 10**6 or nxt_y < 0 or nxt_y >= 10**6: continue 
                    if (nxt_x, nxt_y) in blocked: continue 
                    if (nxt_x, nxt_y) in visited: continue 
                    if (nxt_x, nxt_y) == end: return True 
                    queue.append((nxt_x, nxt_y))
                    visited.add((nxt_x, nxt_y))
            if len(queue) > 0:
                return True 
            else:
                return False 
        return bfs(tuple(source), tuple(target)) and bfs(tuple(target), tuple(source))
        
            
  
# @lc code=end

