#
# @lc app=leetcode id=2101 lang=python3
#
# [2101] Detonate the Maximum Bombs
#

# @lc code=start
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        next = [list() for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: continue 
                x_i, y_i, r_i = bombs[i]
                x_j, y_j, r_j = bombs[j]
                if (x_i - x_j)**2 + (y_i - y_j)**2 <= r_i**2:
                    next[i].append(j)

        ans = 0
        for i in range(n):
            queue = deque()
            queue.append(i)
            visited = [False] * n
            visited[i] = True
            count = 0
            while queue:
                curr = queue.popleft()
                count += 1
                for nxt in next[curr]:
                    if visited[nxt]: continue
                    queue.append(nxt)
                    visited[nxt] = True

            ans = max(ans, count)
        return ans
# @lc code=end

