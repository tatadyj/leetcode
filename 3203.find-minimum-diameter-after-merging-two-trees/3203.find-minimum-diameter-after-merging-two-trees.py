#
# @lc app=leetcode id=3203 lang=python3
#
# [3203] Find Minimum Diameter After Merging Two Trees
#

# @lc code=start
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def treeDiameter(edges: List[List[int]]) -> int:
            adj_dict = defaultdict(list)
            for a,b in edges:
                adj_dict[a].append(b)
                adj_dict[b].append(a)
            n = len(edges) + 1

            def bfs(start):
                queue = deque()
                queue.append(start)
                dist = [-1] * n
                dist[start] = 0 
                max_dist = 0 
                max_node = start

                while queue:
                    curr = queue.popleft()
                    for nxt in adj_dict[curr]:
                        if dist[nxt] != -1: continue 
                        queue.append(nxt)
                        dist[nxt] = dist[curr] + 1
                        if dist[nxt] > max_dist:
                            max_dist = dist[nxt]
                            max_node = nxt 
                return max_node, max_dist

            B, _ = bfs(0)
            C, res = bfs(B)
            return res
            
        d1 = treeDiameter(edges1)
        d2 = treeDiameter(edges2)
        return max(d1, d2, (d1+1) // 2 + (d2+1) // 2 + 1)  
# @lc code=end

