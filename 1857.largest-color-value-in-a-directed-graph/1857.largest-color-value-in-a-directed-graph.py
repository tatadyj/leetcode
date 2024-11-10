#
# @lc app=leetcode id=1857 lang=python3
#
# [1857] Largest Color Value in a Directed Graph
#

# @lc code=start
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj_dict = defaultdict(list)
        in_degree = [0] * n
        for a,b in edges:
            adj_dict[a].append(b)
            in_degree[b] += 1

        def bfs(c, in_degree):
            count = [0] * n
            queue = deque()
            for i in range(n):
                if in_degree[i] == 0:
                    queue.append(i)
                    if colors[i] == c:
                        count[i] += 1 # all nodes with same color have count == 1

            while queue:
                curr = queue.popleft()
                for nxt in adj_dict[curr]:
                    # 多条路径中选最大 count[nxt]
                    # BFS count 套路 
                    if colors[nxt] == c:
                        count[nxt] = max(count[nxt], 1 + count[curr])
                    else:
                        count[nxt] = max(count[nxt], count[curr])
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        queue.append(nxt)
            
            for i in range(n):
                if in_degree[i] != 0:
                    return -1
            return max(count)

        ans = 0
        for c in set(colors):
            res = bfs(c, in_degree.copy())
            if res == -1:
                return -1
            ans = max(ans, res)
        return ans 
# @lc code=end

