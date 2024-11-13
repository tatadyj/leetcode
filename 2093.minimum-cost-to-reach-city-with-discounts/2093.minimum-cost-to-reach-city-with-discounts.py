#
# @lc app=leetcode id=2093 lang=python3
#
# [2093] Minimum Cost to Reach City With Discounts
#

# @lc code=start
class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        adj_dict = defaultdict(list)
        for a, b, t in highways:
            adj_dict[a].append((b, t))
            adj_dict[b].append((a, t))

        memo = [[False] * (discounts+1) for i in range(n)] # memo[city][discount]
        pq = [(0, 0, 0)] # cost, city, used_discount 

        while pq:
            cost, curr_city, used_discount = heapq.heappop(pq)
            if memo[curr_city][used_discount]: continue 
            memo[curr_city][used_discount] = True
            
            if curr_city == n-1:
                return cost 

            for nxt_city, nxt_cost in adj_dict[curr_city]:
                if memo[nxt_city][used_discount]: continue
                heapq.heappush(pq, (nxt_cost+cost, nxt_city, used_discount))
                if used_discount + 1 > discounts: continue 
                if memo[nxt_city][used_discount + 1]: continue 
                heapq.heappush(pq, (nxt_cost//2+cost, nxt_city, used_discount+1))
        return -1 
# @lc code=end

