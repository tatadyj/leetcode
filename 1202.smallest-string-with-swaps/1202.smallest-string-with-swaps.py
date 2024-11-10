#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = Union_Find(n)
        for a,b in pairs:
            uf.union(a, b)

        freq = defaultdict(list)
        idx = defaultdict(list)
        for i in range(n):
            p = uf.find(i)
            freq[p].append(s[i])
            idx[p].append(i)

        for key in freq:
            freq[key].sort()
            idx[key].sort()

        ans = [None] * n
        for key in freq:
            for j in range(len(freq[key])):
                ans[idx[key][j]] = freq[key][j]
        return ''.join(ans)
            


        
        
# @lc code=end

