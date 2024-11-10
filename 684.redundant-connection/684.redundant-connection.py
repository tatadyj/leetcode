#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
class Union_Find:
    def __init__(self, n):
        self.parent = {i:i for i in range(1, n+1)}

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_i, node_j):
        root_i = self.find(node_i)
        root_j = self.find(node_j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            return True 
        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max([max(e) for e in edges])
        uf = Union_Find(n)
        for node_i, node_j in edges:
            if uf.union(node_i, node_j):
                continue 
            else:
                return [node_i, node_j]

           
# @lc code=end

