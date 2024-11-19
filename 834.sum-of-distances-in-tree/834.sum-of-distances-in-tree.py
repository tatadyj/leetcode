#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#

# @lc code=start
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_dict = defaultdict(list)
        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        
        subtree = [1] * n
        def dfs_subtree(curr, prev):
            
            for nxt in adj_dict[curr]:
                if nxt == prev: continue
                dfs_subtree(nxt, curr)
                subtree[curr] += subtree[nxt]

        dfs_subtree(0, -1)
        
        distance_to_root = [0] * n
        def dfs_distance(curr, prev):

            for nxt in adj_dict[curr]:
                if nxt == prev: continue 
                distance_to_root[nxt] = distance_to_root[curr] + 1
                dfs_distance(nxt, curr)

        dfs_distance(0, -1)

        ans = [0] * n 
        ans[0] = sum(distance_to_root)
        def dfs(curr, prev):
            for nxt in adj_dict[curr]:
                if nxt == prev: continue 
                ans[nxt] = ans[curr] - subtree[nxt] + (n - subtree[nxt])
                dfs(nxt, curr)
        dfs(0, -1)
        return ans   
# @lc code=end

