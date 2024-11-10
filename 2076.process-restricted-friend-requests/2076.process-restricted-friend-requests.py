#
# @lc app=leetcode id=2076 lang=python3
#
# [2076] Process Restricted Friend Requests
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
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        uf = Union_Find(n)
        res = []
        for u,v in requests:
            u_root, v_root = uf.find(u), uf.find(v)

            if u_root == v_root:
                res.append(True)
                continue

            flag = 0
            for x,y in restrictions:
                x_root, y_root = uf.find(x), uf.find(y)
                if (u_root == x_root and v_root == y_root) or (v_root == x_root and u_root == y_root):
                    flag = 1
                    break 
            
            res.append(flag==0)
            if flag == 0:
                uf.union(u, v)

        return res  
# @lc code=end

