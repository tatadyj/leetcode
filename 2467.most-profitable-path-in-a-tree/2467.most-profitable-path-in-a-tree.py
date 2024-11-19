#
# @lc app=leetcode id=2467 lang=python3
#
# [2467] Most Profitable Path in a Tree
#

# @lc code=start
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        #adjacency list
        adj_dict = defaultdict(list)
        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        n = max(adj_dict.keys()) + 1
        bob_path = [float('inf')] * n
        def dfs_bob(curr, prev):
            nonlocal ans
            if curr == bob:
                ans = path[:]
                return 

            for nxt in adj_dict[curr]:
                if nxt != prev:
                    path.append(nxt)
                    dfs_bob(nxt, curr)
                    path.pop()

        def dfs_alice(score, curr, prev, step):
            nonlocal res
            if step == bob_path[curr]:
                score += amount[curr] // 2
            elif step < bob_path[curr]:
                score += amount[curr]
    
            if len(adj_dict[curr]) == 1 and adj_dict[curr][0] == prev:
                res = max(res, score)
                return 

            for nxt in adj_dict[curr]:
                if nxt != prev:
                    dfs_alice(score, nxt, curr, step+1)

        ans, path = [], [0]
        dfs_bob(0, -1)
        for step,node in enumerate(ans[::-1]):
            bob_path[node] = step

        res = float('-inf')
        dfs_alice(0, 0, -1, 0)
        return res  
# @lc code=end

