#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#

# @lc code=start
class Union_Find():
    def __init__(self, stones):
        self.n = len(stones)
        self.parent = defaultdict(tuple)
        self.rank = defaultdict(int)

        for x, y in stones:
            self.parent[(x, y)] = (x, y)
            self.rank[(x, y)] = 1

        self.count = self.n
    
    def find(self, stone):
        if self.parent[stone] == stone:
            return stone 
        else:
            self.parent[stone] = self.find(self.parent[stone])
            return self.parent[stone]

    def union(self, stone_i, stone_j):
        root_i = self.find(stone_i)
        root_j = self.find(stone_j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            self.count -= 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones = [(x,y) for x,y in stones]
        uf = Union_Find(stones)
        for i in range(uf.n):
            for j in range(i+1, uf.n):
                xi, yi = stones[i]
                xj, yj = stones[j]
                if xi == xj or yi == yj:
                    uf.union(stones[i], stones[j])

        return uf.n - uf.count
          
# @lc code=end

