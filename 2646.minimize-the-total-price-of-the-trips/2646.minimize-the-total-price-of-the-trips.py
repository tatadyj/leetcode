#
# @lc app=leetcode id=2646 lang=python3
#
# [2646] Minimize the Total Price of the Trips
#

# @lc code=start
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        adj_dict = defaultdict(list)
        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        count = [0] * n

        def dfs(curr, prev, target):
            if curr == target:   
                count[curr] += 1
                return True 

            for nxt in adj_dict[curr]:
                if nxt != prev:
                    if dfs(nxt, curr, target):
                        count[curr] += 1
                        return True 
            
            return False
        
        for start, end in trips:
            dfs(start, -1, end)

        for i in range(n):
            price[i] = price[i] * count[i]

        plan1 = [None] * n # flag 1, the node is free to select or not 
        plan0 = [None] * n # flag 0, the node can not be select
        def dfs_hr(curr, prev, flag):
            if flag == 1:
                if plan1[curr] is not None:
                    return plan1[curr]
                opt1, opt2 = price[curr] // 2, price[curr]
                for nxt in adj_dict[curr]:
                    if nxt == prev: continue
                    opt1 += dfs_hr(nxt, curr, 0)
                    opt2 += dfs_hr(nxt, curr, 1)
                res = min(opt1, opt2)
                plan1[curr] = res
                return res 
            if flag == 0:
                if plan0[curr] is not None:
                    return plan0[curr]
                res = price[curr] 
                for nxt in adj_dict[curr]:
                    if nxt == prev: continue
                    res += dfs_hr(nxt, curr, 1)
                plan0[curr] = res
                return res

        return dfs_hr(0, -1, 1)
       
# @lc code=end

