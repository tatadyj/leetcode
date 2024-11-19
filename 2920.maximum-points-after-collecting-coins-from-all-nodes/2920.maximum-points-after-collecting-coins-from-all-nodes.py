#
# @lc app=leetcode id=2920 lang=python3
#
# [2920] Maximum Points After Collecting Coins From All Nodes
#

# @lc code=start
class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        adj_dict = defaultdict(list)
        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        n = len(adj_dict.keys())
        memo = [[None] * 14 for _ in range(n)] # ceil(math.log2(10**4)) == 14 

        def get_coins(c, cuts):
            for i in range(cuts):
                c = c // 2
            return c

        def dfs(curr, prev, cuts):
            if cuts > 13:
                cuts = 13

            if memo[curr][cuts] is not None:
                return memo[curr][cuts]

            cns = get_coins(coins[curr], cuts)
            sum1 = cns - k
            sum2 = cns // 2

            for nxt in adj_dict[curr]:
                if nxt != prev:
                    sum1 += dfs(nxt, curr, cuts)
                    sum2 += dfs(nxt, curr, cuts+1)

            val = max(sum1, sum2)
            memo[curr][cuts] = val 
            return val 

        return dfs(0, -1, 0)
# @lc code=end

