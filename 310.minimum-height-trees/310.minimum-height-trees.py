#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
def dfs_tle():
        adj_dict = defaultdict(list)
        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        def dfs(curr, prev):
            h = -1
            for nxt in adj_dict[curr]:
                if nxt == prev: continue 
                h = max(h, dfs(nxt, curr))
            return h + 1

        heights = []
        for root in range(n):
            height = dfs(root, -1)
            heights.append(height)
        min_height = min(heights)
        return [i for i,h in enumerate(heights) if h == min_height]

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        if n == 2: return [0, 1]
        adj_dict = defaultdict(list)
        degree = [0] * n
        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        count = 0
        while len(queue):
            size = len(queue)
            for _ in range(size): # 需要把下一层的都加入queue
                curr = queue.popleft()
                count += 1
                for nxt in adj_dict[curr]:
                    degree[nxt] -= 1
                    if degree[nxt] == 1:
                        queue.append(nxt)
            if count == n - 1 or count == n - 2:
                break 

        return list(queue) 
# @lc code=end

