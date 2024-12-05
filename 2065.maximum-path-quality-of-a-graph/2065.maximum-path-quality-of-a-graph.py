#
# @lc app=leetcode id=2065 lang=python3
#
# [2065] Maximum Path Quality of a Graph
#

# @lc code=start
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        adj_dict = defaultdict(list)
        for a, b, t in edges:
            adj_dict[a].append((b, t))
            adj_dict[b].append((a, t))

        visited = [False] * len(values)
        ans = 0
        def dfs(curr, total_time, quality):
            nonlocal ans
            if total_time > maxTime:
                return 

            if curr == 0:
                ans = max(ans, quality)

            for nxt, nxt_time in adj_dict[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    dfs(nxt, total_time+nxt_time, quality + values[nxt])
                    visited[nxt] = False
                else: # 注意不用更新visited 
                    dfs(nxt, total_time+nxt_time, quality)
        visited[0] = True
        dfs(0, 0, values[0])
        return ans
           
# @lc code=end

