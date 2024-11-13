#
# @lc app=leetcode id=2045 lang=python3
#
# [2045] Second Minimum Time to Reach Destination
#

# @lc code=start
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj_dict = defaultdict(list)
        for a, b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        queue = deque()
        queue.append((1, 0)) # node, time
        visited = [0] * (n + 1)
        dist = [-1] * (n + 1)
        visited[1] = 1
        dist[1] = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                curr, t = queue.popleft()
                if (t // change) % 2 == 0: # green
                    nxt_t = t + time 
                if (t // change) % 2 == 1: # red
                    nxt_t = (t // change + 1) * change + time

                for nxt in adj_dict[curr]:
                    if visited[nxt] < 2 and dist[nxt] < nxt_t: # 第二次到达时间
                        dist[nxt] = nxt_t
                        queue.append((nxt, nxt_t))
                        visited[nxt] += 1

                    if nxt == n and visited[nxt] == 2:
                        return nxt_t 
        return -1   
# @lc code=end

