#
# @lc app=leetcode id=2204 lang=python3
#
# [2204] Distance to a Cycle in Undirected Graph
#

# @lc code=start
class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_dict = defaultdict(list)
        degree = [0] * n
        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)
            degree[a] += 1
            degree[b] += 1

        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        ans = [0] * n
        while queue:
            curr = queue.pop()
            ans[curr] = -1
            for nxt in adj_dict[curr]:
                degree[nxt] -= 1
                if degree[nxt] == 1:
                    queue.append(nxt)

        q = deque()
        for i in range(n):
            if ans[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            for nxt in adj_dict[cur]:
                if ans[nxt] == -1:
                    ans[nxt] = ans[cur] + 1
                    q.append(nxt)

        return ans
   
# @lc code=end

