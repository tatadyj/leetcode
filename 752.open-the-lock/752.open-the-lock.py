#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        if '0000' == target:
            return 0

        queue = deque()
        queue.append(('0000', 0))
        visited = set('0000')

        def next(curr):
            res = []
            for i in range(4):
                for j in [1, -1]:
                    new = curr[:i] + str((int(curr[i]) + j) % 10) + curr[i+1:] 
                    res.append(new)
            return res

        while queue:
            size = len(queue)
            for _ in range(size):
                curr, level = queue.popleft()
                for nxt in next(curr):
                    if nxt in deadends: continue 
                    if nxt in visited: continue 
                    if nxt == target:
                        return level + 1 
                    queue.append((nxt, level+1))
                    visited.add(nxt)
        return -1
        
# @lc code=end

