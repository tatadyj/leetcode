#
# @lc app=leetcode id=2473 lang=python3
#
# [2473] Minimum Cost to Buy Apples
#

# @lc code=start
class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        appleCost.insert(0, 0)
        adj_dict = defaultdict(list)
        for a, b, c in roads:
            adj_dict[a].append((b, c))
            adj_dict[b].append((a, c))

        ans = []
        for s in range(1, n+1):
            ret = inf
            dist = [-1] * (n+1)
            pq = [(0, s)]

            while pq:
                w, cur = heapq.heappop(pq)
                if dist[cur] != -1: continue 
                dist[cur] = w 
                ret = min(ret, w * (k+1) + appleCost[cur])
                for nxt, nxt_w in adj_dict[cur]:
                    if dist[nxt] != -1: continue
                    heapq.heappush(pq, (w + nxt_w, nxt))
            
            ans.append(ret)
        return ans  
# @lc code=end

