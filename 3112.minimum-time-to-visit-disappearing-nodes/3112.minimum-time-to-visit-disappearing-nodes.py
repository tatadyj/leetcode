#
# @lc app=leetcode id=3112 lang=python3
#
# [3112] Minimum Time to Visit Disappearing Nodes
#

# @lc code=start
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        adj_dict = defaultdict(list)
        for a, b, w in edges:
            adj_dict[a].append((b, w))
            adj_dict[b].append((a, w))

        ans = [-1] * n
        pq = [(0, 0)]

        while pq:
            w, cur = heapq.heappop(pq)
            if ans[cur] != -1: continue 
            #if disappear[cur] > w:
            ans[cur] = w 

            for nxt, nxt_w in adj_dict[cur]:
                if ans[nxt] != -1: continue 
                if disappear[nxt] <= w + nxt_w: continue 
                heapq.heappush(pq, (w + nxt_w, nxt))    

        return ans  
# @lc code=end

