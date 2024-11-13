#
# @lc app=leetcode id=1617 lang=python3
#
# [1617] Count Subtrees With Max Distance Between Cities
#

# @lc code=start
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_dict = defaultdict(list)
        for a,b in edges:
            adj_dict[a-1].append(b-1) # 0-indexd
            adj_dict[b-1].append(a-1)

        def bfs(start):
            dist = [-1] * n
            queue = deque()
            queue.append(start)
            dist[start] = 0
            max_dist = 0
            max_node = start

            while queue:
                curr = queue.popleft()
                for nxt in adj_dict[curr]:
                    if allow[nxt] == 0: continue 
                    if dist[nxt] == -1:
                        queue.append(nxt)
                        dist[nxt] = dist[curr] + 1
                        if dist[nxt] > max_dist:
                            max_dist = dist[nxt]
                            max_node = nxt
            return max_node, dist
        
        diameter = [0] * n # d from 1 to n-1
        for state in range(1, 1<<n): # [1, 2**15]
            count_ones = 0
            allow = [0] * n
            for i in range(n):
                if (state >> i) & 1 == 1: 
                    allow[i] = 1
                    count_ones += 1
                    A = i
                else:
                    allow[i] = 0
            
            B, dist = bfs(A)
            num_visited = sum([d != -1 for d in dist])
            if num_visited != count_ones: continue
            C, dist = bfs(B)
            max_diameter = max(dist)
            diameter[max_diameter] += 1
        return diameter[1:]
# @lc code=end

