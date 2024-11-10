#
# @lc app=leetcode id=2421 lang=python3
#
# [2421] Number of Good Paths
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
        if x_root < y_root:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root


def sol1(self, vals: List[int], edges: List[List[int]]) -> int:
    n = len(vals)
    uf = Union_Find(n)

    edge_map = defaultdict(list)
    for a, b in edges:
        if vals[a] > vals[b]:
            edge_map[vals[a]].append((a, b))
        else:
            edge_map[vals[b]].append((b, a))

    val2idx = defaultdict(list)
    for i in range(n):
        val2idx[vals[i]].append(i)

    ans = 0
    unique_vals = sorted(list(set(vals)))
    for v in unique_vals:
        for a, b in edge_map[v]:
            uf.union(a, b)

        count = defaultdict(int)
        for i in val2idx[v]:
            count[uf.find(i)] += 1

        for p in count:
            freq = count[p]
            ans += freq * (freq - 1) // 2
    return ans + n

from sortedcontainers import SortedDict

class DefaultSortedDict(SortedDict):
    def __missing__(self, key):
        value = 0
        self[key] = value
        return value

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        adj_dict = defaultdict(list)
        for a, b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)
        
        def dfs(curr, prev):
            nonlocal ans
            count = DefaultSortedDict()
            count[vals[curr]] += 1
            for nxt in adj_dict[curr]:
                if nxt == prev: continue 
                sd = dfs(nxt, curr)
                idx = sd.bisect_left(vals[curr]) 
                for i in range(idx):
                    sd.popitem(0)
                if len(count) < len(sd):
                    count, sd = sd, count
                for key in sd:
                    if key in count:
                        ans += sd[key] * count[key]
                for key in sd:
                    count[key] += sd[key]
            return count 

        ans = 0
        dfs(0, -1)
        return ans + len(vals)









 
# @lc code=end

