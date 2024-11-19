#
# @lc app=leetcode id=2581 lang=python3
#
# [2581] Count Number of Possible Root Nodes
#

# @lc code=start
class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        adj_dict = defaultdict(list)
        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        guess_dict = defaultdict(set)
        for p,c in guesses:
            guess_dict[p].add(c)

        def dfs(curr, prev):
            count = 0
            for nxt in adj_dict[curr]:
                if nxt == prev: continue 
                count += dfs(nxt, curr)
                if nxt in guess_dict[curr]:
                    count += 1
            return count 

        total_count = dfs(0, -1)
        #print(total_count)

        if total_count >= k:
            ans = 1
        else:
            ans = 0
        #print(ans, total_count)
        def dfs_reroot(curr, prev, total_count):
            nonlocal ans
            for nxt in adj_dict[curr]:
                if nxt == prev: continue
                count = total_count # total_count 对于每个nxt，同一层total_count不能变
                if nxt in guess_dict[curr]:
                    count -= 1
                if curr in guess_dict[nxt]:
                    count += 1
                if count >= k:
                    ans += 1
                    #print(nxt, curr, total_count)
                dfs_reroot(nxt, curr, count)


        dfs_reroot(0, -1, total_count)
        return ans 

        
# @lc code=end

