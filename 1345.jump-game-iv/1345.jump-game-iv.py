#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#

# @lc code=start
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        map = defaultdict(list)
        for i,v in enumerate(arr):
            map[v].append(i)

        queue = deque()
        queue.append((0, 0))
        visited = [False] * n
        visited[0] = True

        while queue:
            size = len(queue)
            for _ in range(size):
                curr, level = queue.popleft()
                if curr + 1 < n and not visited[curr+1]:
                    if curr + 1 == n - 1:
                        return level + 1
                    queue.append((curr+1, level+1))
                    visited[curr+1] = True 
                if curr - 1 >= 0 and not visited[curr-1]:
                    if curr - 1 == n-1:
                        return level + 1
                    queue.append((curr-1, level+1))
                    visited[curr-1] = True 
                for nxt in map[arr[curr]]:
                    #if nxt == curr: continue 
                    if visited[nxt]: continue 
                    if nxt == n-1:
                        return level + 1
                    queue.append((nxt, level+1))
                    visited[nxt] = True 
                map.pop(arr[curr])   
# @lc code=end

