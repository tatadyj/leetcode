#
# @lc app=leetcode id=851 lang=python3
#
# [851] Loud and Rich
#

# @lc code=start
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adj_dict = defaultdict(list)
        in_degree = [0] * n
        for a, b in richer:
            adj_dict[a].append(b)
            in_degree[b] += 1

        map = defaultdict(int)
        for i,q in enumerate(quiet):
            map[q] = i

        ans = [None] * n
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            ans[curr] = map[quiet[curr]]
            for nxt in adj_dict[curr]:
                in_degree[nxt] -= 1
                quiet[nxt] = min(quiet[nxt], quiet[curr])
                if in_degree[nxt] == 0:
                    queue.append(nxt)
        return ans
         
     
# @lc code=end

