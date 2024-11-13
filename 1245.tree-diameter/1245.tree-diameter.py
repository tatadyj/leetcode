#
# @lc app=leetcode id=1245 lang=python3
#
# [1245] Tree Diameter
#

# @lc code=start
def dfs_method(self, edges: List[List[int]]) -> int:
    adj_dict = defaultdict(list)
    for a,b in edges:
        adj_dict[a].append(b)
        adj_dict[b].append(a)

    ans = 0
    def dfs(curr, prev):
        nonlocal ans

        length = []
        for nxt in adj_dict[curr]:
            if nxt != prev:
                length.append(dfs(nxt, curr))
        length.sort(reverse=True)
        if len(length) >= 2:
            diameter = sum(length[:2])
        elif len(length) == 1:
            diameter = length[0] 
        else:
            diameter = 0
        ans = max(ans, diameter)
        return max(length) + 1 if len(length) > 0 else 1 

    dfs(0, -1)
    return ans

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
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

            
# @lc code=end

