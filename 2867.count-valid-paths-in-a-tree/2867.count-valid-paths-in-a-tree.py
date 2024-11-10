#
# @lc app=leetcode id=2867 lang=python3
#
# [2867] Count Valid Paths in a Tree
#

# @lc code=start
def all_primes(n):
    if n <= 2:
        return []

    numbers = [False, False] + [True] * (n - 2)
    for p in range(2, int(sqrt(n)) + 1):
        if numbers[p]:
            for multiple in range(p * p, n, p):
                numbers[multiple] = False 
            
    return [i for i,v in enumerate(numbers) if v]

class Union_Find:
    def __init__(self, n):
        self.n = n 
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

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
        self.size[x_root] += self.size[y_root]

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        adj_dict = defaultdict(list)
        for a, b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        primes = all_primes(n+1)
        primes = set(primes)

        uf = Union_Find(n+1)
        for a, b in edges:
            if a not in primes and b not in primes:
                uf.union(a, b)

        res = 0
        for p in primes:
            arr = []
            for nxt in adj_dict[p]:
                if nxt not in primes:
                    arr.append(uf.size[uf.find(nxt)]) 
            total = sum(arr)
            accum = 0 
            for v in arr:
                accum += v * (total - v)
            res += accum // 2 + total 
        return res 
        
# @lc code=end

