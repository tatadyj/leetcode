#
# @lc app=leetcode id=1722 lang=python3
#
# [1722] Minimize Hamming Distance After Swap Operations
#

# @lc code=start
from sortedcontainers import SortedList

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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(target)
        uf = Union_Find(n)
        for a, b in allowedSwaps:
            uf.union(a, b)

        freq = defaultdict(list)
        for i in range(n):
            freq[uf.find(i)].append(i)

        count = 0
        for p in freq:
            s = defaultdict(int) 
            for i in freq[p]:
                s[source[i]] += 1

            t = defaultdict(int) 
            for i in freq[p]:
                t[target[i]] += 1

            for k in t:
                count += min(t[k], s[k])
        return len(target) - count
# @lc code=end

