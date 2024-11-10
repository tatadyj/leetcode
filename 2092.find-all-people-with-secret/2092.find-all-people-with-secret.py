#
# @lc app=leetcode id=2092 lang=python3
#
# [2092] Find All People With Secret
#

# @lc code=start
class Union_Find:
    def __init__(self, n, firstPerson):
        self.n = n 
        self.parent = [i for i in range(n)]
        self.parent[firstPerson] = 0
  
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


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        uf = Union_Find(n, firstPerson)
        known = set([firstPerson, 0])
        i = 0 
        while i < len(meetings):
            group = set()
            j = i
            while j < len(meetings) and meetings[j][2] == meetings[i][2]:
                a, b, _ = meetings[j]
                uf.union(a, b)
                group.add(a)
                group.add(b)
                j += 1
        
            for g in group:
                if uf.find(g) == 0:
                    known.add(g)
                else:
                    uf.parent[g] = g
            i = j
        return list(known)

# @lc code=end

