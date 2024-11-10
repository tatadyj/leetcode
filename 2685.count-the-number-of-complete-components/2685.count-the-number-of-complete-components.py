#
# @lc app=leetcode id=2685 lang=python3
#
# [2685] Count the Number of Complete Components
#

# @lc code=start
class Union_Find:
    def __init__(self, n):
        self.n = n 
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return x 
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root > y_root:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = Union_Find(n)
        for a, b in edges:
            uf.union(a, b)
        
        count_nodes = defaultdict(int)
        for i in range(n):
            count_nodes[uf.find(i)] += 1

        count_edges = defaultdict(set)
        for a, b in edges:
            count_edges[uf.find(a)].add((a,b))

        res = 0
        for p in count_nodes:
            n_node = count_nodes[p]
            n_edge = len(count_edges[p])
            if n_edge == n_node * (n_node - 1) / 2:
                res += 1
        return res 
# @lc code=end

