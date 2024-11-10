#
# @lc app=leetcode id=1591 lang=python3
#
# [1591] Strange Printer II
#

# @lc code=start
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m = len(targetGrid)
        n = len(targetGrid[0])

        color_bdry = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if targetGrid[i][j] not in color_bdry:
                    color_bdry[targetGrid[i][j]] = [i, i, j, j] # 上下左右
                else:
                    color_bdry[targetGrid[i][j]][0] = min(color_bdry[targetGrid[i][j]][0], i)
                    color_bdry[targetGrid[i][j]][1] = max(color_bdry[targetGrid[i][j]][1], i)
                    color_bdry[targetGrid[i][j]][2] = min(color_bdry[targetGrid[i][j]][2], j)
                    color_bdry[targetGrid[i][j]][3] = max(color_bdry[targetGrid[i][j]][3], j)

        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for c in color_bdry:
            in_degree[c] = 0

        for i in range(m):
            for j in range(n):
                for c in color_bdry:
                    top, bottom, left, right = color_bdry[c]
                    if i >= top and i <= bottom and j >= left and j <= right:
                        if c != targetGrid[i][j] and c not in graph[targetGrid[i][j]]:
                            graph[targetGrid[i][j]].append(c)
                            in_degree[c] += 1

        queue = deque()
        for c in in_degree:
            if in_degree[c] == 0:
                queue.append(c)

        count = 0
        while queue:
            curr = queue.popleft()
            count += 1
            for nxt in graph[curr]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)
        if count != len(in_degree):
            return False 
        return True 
  
# @lc code=end

