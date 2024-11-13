#
# @lc app=leetcode id=2493 lang=python3
#
# [2493] Divide Nodes Into the Maximum Number of Groups
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
        self.parent[y_root] = x_root

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj_dict = defaultdict(list)
        for a, b in edges:
            adj_dict[a-1].append(b-1)
            adj_dict[b-1].append(a-1)

        uf = Union_Find(n)
        for a, b in edges:
            uf.union(a-1, b-1)

        map = defaultdict(set)
        for i in range(n):
            map[uf.find(i)].add(i)

        def bfs(root):
            queue = deque()
            queue.append((root, 0))
            level = [-1] * n 
            level[root] = 0 
            ret = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    curr, lvl = queue.popleft()
                    ret = max(ret, lvl)
                    for nxt in adj_dict[curr]:
                        if nxt not in map[gp]: continue 
                        if level[nxt] == lvl:
                            return -1
                        elif level[nxt] != -1:
                            continue 
                        else:
                            queue.append((nxt, lvl+1))
                            level[nxt] = lvl + 1 
            return ret + 1

        ans = 0
        for gp in map:
            max_val = 0
            for root in map[gp]:
                res = bfs(root)
                if res == -1: return -1 
                max_val = max(max_val, res)
            ans += max_val 
        return ans   
# @lc code=end

