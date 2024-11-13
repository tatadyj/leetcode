#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = deque()
        queue.append((startGene, 0))
        visited = set()
        visited.add(startGene)
        while queue:
            curr, lvl = queue.popleft()
            for i in range(8):
                for s in 'ACTG':
                    if s == curr[i]: continue
                    nxt = curr[:i] + s + curr[i+1:]
                    if nxt not in bank: continue 
                    if nxt in visited: continue 
                    if nxt == endGene:
                        return lvl + 1
                    queue.append((nxt, lvl+1))
                    visited.add(nxt)
        return -1      
# @lc code=end

