#
# @lc app=leetcode id=2925 lang=python3
#
# [2925] Maximum Score After Applying Operations on a Tree
#

# @lc code=start
class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        adj_dict = defaultdict(list)
        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        n = len(adj_dict.keys())
        subtree = [0] * n
        def dfs_sum(curr, prev):
            sum = values[curr]
            for nxt in adj_dict[curr]:
                if nxt != prev:
                    sum += dfs_sum(nxt, curr)

            subtree[curr] = sum 
            return sum 

        def dfs(curr, prev):
            if len(adj_dict[curr]) == 1 and adj_dict[curr][0] == prev:
                return 0

            sum1 = values[curr]
            for nxt in adj_dict[curr]:
                if nxt != prev:
                    sum1 += dfs(nxt, curr)
            
            sum2 = subtree[curr] - values[curr] # curr 不取， 其子节点都取
            return max(sum1, sum2)

        dfs_sum(0, -1)
        #print(subtree)
        return dfs(0, -1)  
# @lc code=end

