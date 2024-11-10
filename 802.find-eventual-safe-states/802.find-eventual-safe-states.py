#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out_degree = [0] * n 

        prev_dict = defaultdict(list)
        for prev, nxts in enumerate(graph):
            out_degree[prev] = len(nxts)
            for nxt in nxts:
                prev_dict[nxt].append(prev) 

        queue = deque()
        for i in range(n):
            if out_degree[i] == 0:
                queue.append(i)

        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for prev in prev_dict[curr]:
                out_degree[prev] -= 1
                if out_degree[prev] == 0:
                    queue.append(prev)

        ans.sort()
        return ans
        
# @lc code=end

