#
# @lc app=leetcode id=2714 lang=python3
#
# [2714] Find Shortest Path with K Hops
#

# @lc code=start
class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        adj_dict = defaultdict(list)
        for a, b, w in edges:
            adj_dict[a].append((b, w))
            adj_dict[b].append((a, w))

        pq = [(0, s, 0)]
        memo = [[False] * (k+1) for _ in range(n)]
        while pq:
            w, curr, hops = heapq.heappop(pq)
            if memo[curr][hops]: continue 
            memo[curr][hops] = True 
            if curr == d:
                return w 

            for nxt, nxt_w in adj_dict[curr]:
                if memo[nxt][hops]: continue 
                heapq.heappush(pq, (w+nxt_w, nxt, hops))

            for nxt, nxt_w in adj_dict[curr]:
                if hops + 1 > k: continue
                if memo[nxt][hops+1]: continue 
                heapq.heappush(pq, (w, nxt, hops+1))
 
# @lc code=end

