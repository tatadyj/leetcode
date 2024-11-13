#
# @lc app=leetcode id=1654 lang=python3
#
# [1654] Minimum Jumps to Reach Home
#

# @lc code=start
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0: return 0
        queue = deque()
        queue.append((0, 0, 0)) # 0: right, 1: left
        limit = max(x, max(forbidden)) + b 
        n = 6001
        visited = [[False]*2 for _ in range(n)]
        visited[0][0] = True 
        for f in forbidden:
            visited[f][0] = True 
            visited[f][1] = True 

        while queue:
            size = len(queue)
            for _ in range(size):
                curr, d, l = queue.popleft()
                #print(curr, d, l)
                if d == 0 and curr-b >= 0 and not visited[curr-b][1]: # to left 
                    nxt = curr - b 
                    if nxt == x:
                        return l + 1 
                    queue.append((nxt, 1, l+1))
                    visited[nxt][1] = True
                if curr <= limit and not visited[curr+a][0]: # to right
                    nxt = curr + a 
                    if nxt == x:
                        return l + 1 
                    queue.append((nxt, 0, l+1))
                    visited[nxt][0] = True 
        return -1

   
# @lc code=end

