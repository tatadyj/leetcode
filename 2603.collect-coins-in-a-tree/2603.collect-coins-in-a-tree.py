#
# @lc app=leetcode id=2603 lang=python3
#
# [2603] Collect Coins in a Tree
#

# @lc code=start
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        adj_dict = defaultdict(set)
        degree = [0] * n

        for a, b in edges:
            adj_dict[a].add(b)
            adj_dict[b].add(a)
            degree[a] += 1
            degree[b] += 1

        queue = deque()
        for i in range(n):
            if degree[i] == 1 and coins[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            for nxt in adj_dict[curr]:
                degree[nxt] -= 1
                if degree[nxt] == 1 and coins[nxt] == 0: 
                    queue.append(nxt)
                      
        depth = [0] * n 
        q = deque()
        for i in range(n):
            if degree[i] == 1 and coins[i] == 1:
                q.append((i, 0))
                depth[i] = 0
        while q:
            size = len(q)
            for _ in range(size):
                cur, l = q.popleft()
                depth[cur] = max(depth[cur], l)
                for nei in adj_dict[cur]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append((nei, l+1))

        m = 0 
        for i in range(n):
            m += depth[i] >= 2
        if m == 0:
            return 0 
        else:
            return (m-1) * 2  
# @lc code=end

