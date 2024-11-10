#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
def binary_search(self, heights: List[List[int]]) -> int:
    def is_ok(val):
        m = len(heights)
        n = len(heights[0])
        queue = deque([(0, 0)])
        dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[0] * n for _ in range(m)]
        visited[0][0] = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_i, curr_j = queue.popleft()
                for d in dr:
                    next_i, next_j = curr_i + d[0], curr_j + d[1]
                    if next_i >= 0 and next_i < m and next_j >= 0 and next_j < n \
                        and visited[next_i][next_j] == False \
                        and abs(heights[curr_i][curr_j] - heights[next_i][next_j]) <= val:
                        queue.append((next_i, next_j))
                        visited[next_i][next_j] = 1

        return visited[m-1][n-1] == True 

    left = 0 
    right = max([max(e) for e in heights])
    while left < right:
        mid = (left + right) // 2
        if is_ok(mid):
            right = mid 
        else:
            left = mid + 1
    return left 

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
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        if m*n == 1:
            return 0

        uf = Union_Find(m*n)
        edges = defaultdict(list)
        for i in range(m):
            for j in range(n-1):
                d = abs(heights[i][j] - heights[i][j+1])
                edges[d].append((i*n+j, i*n+(j+1)))
        
        for i in range(m-1):
            for j in range(n):
                d = abs(heights[i][j] - heights[i+1][j])
                edges[d].append((i*n+j, (i+1)*n+j))

        for e in sorted(edges):
            for a, b in edges[e]:
                uf.union(a, b)
                if uf.find(0) == uf.find(m*n-1):
                    return e

        
# @lc code=end

