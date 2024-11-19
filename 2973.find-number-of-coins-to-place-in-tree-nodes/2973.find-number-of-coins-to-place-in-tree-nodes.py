#
# @lc app=leetcode id=2973 lang=python3
#
# [2973] Find Number of Coins to Place in Tree Nodes
#

# @lc code=start
class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:        
        adj_dict = defaultdict(list)
        subtree = defaultdict(list)

        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        def dfs(curr, prev):
            arr = []
            for nxt in adj_dict[curr]:
                if nxt != prev:
                    dfs(nxt, curr)
                    arr.extend(subtree[nxt])
            arr.append(cost[curr])
            arr.sort()

            if len(arr) < 3:
                res[curr] = 1
            else:
                res[curr] = max(0, max(arr[-3]*arr[-2]*arr[-1], arr[0]*arr[1]*arr[-1]))

            if len(arr) <= 5:
                subtree[curr].extend(arr)
            else:
                subtree[curr].extend([arr[-3], arr[-2], arr[-1], arr[0], arr[1]])

        res = [None] * len(adj_dict.keys())
        dfs(0, -1)
        return res     
# @lc code=end

