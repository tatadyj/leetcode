#
# @lc app=leetcode id=2322 lang=python3
#
# [2322] Minimum Score After Removals on a Tree
#

# @lc code=start
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        adj_dict = defaultdict(list)
        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        n = len(adj_dict.keys())

        def dfs(curr, prev, subtree):
            xor = 0
            for nxt in adj_dict[curr]:
                if nxt == prev: continue
                xor = xor ^ dfs(nxt, curr, subtree)
            xor = xor ^ nums[curr]
            subtree[curr] = xor
            return xor

        ans = float('inf')
        for a,b in edges:
            adj_dict[a].remove(b)
            adj_dict[b].remove(a)

            asubtree = [None] * n
            atotal = dfs(a, -1, asubtree)

            bsubtree = [None] * n
            btotal = dfs(b, -1, bsubtree)

            for i in range(len(bsubtree)):
                if bsubtree[i] is not None and i != b:
                    arr = [atotal, btotal ^ bsubtree[i], bsubtree[i]] # root of subtree need to exclude
                    min_val = min(arr)
                    max_val = max(arr)
                    ans = min(ans, max_val - min_val)
                    #print(a, b, i, min_val, max_val, max_val - min_val)

            for i in range(len(asubtree)):
                if asubtree[i] is not None and i != a:
                    arr = [btotal, atotal ^ asubtree[i], asubtree[i]]
                    min_val = min(arr)
                    max_val = max(arr)
                    ans = min(ans, max_val - min_val)
                    #print(a, b, i, min_val, max_val, max_val - min_val)

            adj_dict[a].append(b)
            adj_dict[b].append(a)
        return ans

# @lc code=end

