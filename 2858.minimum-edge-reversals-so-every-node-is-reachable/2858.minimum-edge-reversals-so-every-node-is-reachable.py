#
# @lc app=leetcode id=2858 lang=python3
#
# [2858] Minimum Edge Reversals So Every Node Is Reachable
#

# @lc code=start
class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_dict = defaultdict(list)
        for a,b in edges:
            adj_dict[a].append((b, 1))
            adj_dict[b].append((a, -1))

        def dfs(curr, prev):
            count_reversal = 0
            for nxt, dir in adj_dict[curr]:
                if nxt == prev: continue
                count_reversal += dfs(nxt, curr)
                if dir == -1:
                    count_reversal += 1
            return count_reversal

        count_reversal = dfs(0, -1)
        #print(count_reversal)

        ans = [0] * n
        ans[0] = count_reversal
        def dfs_reroot(curr, prev, count_reversal):
            for nxt, dir in adj_dict[curr]:
                if nxt == prev: continue
                count = count_reversal 
                if dir == -1:
                    count -= 1
                if dir == 1:
                    count += 1
                ans[nxt] = count
                dfs_reroot(nxt, curr, count)
               
        dfs_reroot(0, -1, count_reversal)
        return ans      
# @lc code=end

