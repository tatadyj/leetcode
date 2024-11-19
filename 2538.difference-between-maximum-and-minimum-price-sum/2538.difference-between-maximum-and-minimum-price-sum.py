#
# @lc app=leetcode id=2538 lang=python3
#
# [2538] Difference Between Maximum and Minimum Price Sum
#

# @lc code=start
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        adj_dict = defaultdict(list)
        for a, b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)
    
        leaf = [0] * n # for each node, max path sum of that node to any leaf node 
        inner = [0] * n # for each node, max path sum of that node to any node just 1 node before leaf node

        def dfs(curr, prev):
            if len(adj_dict[curr]) == 0 or (len(adj_dict[curr]) == 1 and adj_dict[curr][0] == prev):
                leaf[curr] = price[curr]
                inner[curr] = 0
                return (leaf[curr], inner[curr])

            max_sum_leaf, max_sum_inner = 0, 0
            for nxt in adj_dict[curr]:
                if nxt == prev: continue 
                sum_leaf, sum_inner = dfs(nxt, curr)
                max_sum_leaf = max(max_sum_leaf, sum_leaf)
                max_sum_inner = max(max_sum_inner, sum_inner)

            leaf[curr] = max_sum_leaf + price[curr]
            inner[curr] = max_sum_inner + price[curr]
            return (leaf[curr], inner[curr])
                  
        dfs(0, -1)

        ret = 0
        def dfs_max(curr, prev):
            nonlocal ret

            arr_leaf = [(leaf[nxt], nxt) for nxt in adj_dict[curr] if nxt != prev]
            arr_inner = [(inner[nxt], nxt) for nxt in adj_dict[curr] if nxt != prev]

            arr_leaf.sort(reverse=True)
            arr_inner.sort(reverse=True)
            ans = max(inner[curr], leaf[curr]-price[curr]) # curr is leaf node, assign the max sum path to inner node
            # curr also can be a empty node 
            if len(arr_leaf) >= 2:
                if arr_leaf[0][1] != arr_inner[0][1]:
                    ans = price[curr] + arr_leaf[0][0] + arr_inner[0][0]
                else:
                    ans = price[curr] + max(arr_leaf[0][0] + arr_inner[1][0], 
                                            arr_leaf[1][0] + arr_inner[0][0])

            ret = max(ret, ans)

            for nxt in adj_dict[curr]:
                if nxt != prev:
                    dfs_max(nxt, curr)
        
        dfs_max(0, -1)
        return ret

        
# @lc code=end

