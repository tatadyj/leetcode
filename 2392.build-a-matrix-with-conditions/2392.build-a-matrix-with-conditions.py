#
# @lc app=leetcode id=2392 lang=python3
#
# [2392] Build a Matrix With Conditions
#

# @lc code=start
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(conditions):
            adj_dict = defaultdict(list)
            in_degree = [0] * (k+1)
            for a, b in conditions:
                adj_dict[a].append(b)
                in_degree[b] += 1

            queue = deque()
            for i in range(1, k+1):
                if in_degree[i] == 0:
                    queue.append(i)

            ret = defaultdict(int)
            count = 0
            while queue:
                curr = queue.popleft()
                ret[curr] = count 
                count += 1
                for nxt in adj_dict[curr]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        queue.append(nxt)

            return ret

        rows = topo_sort(rowConditions)
        cols = topo_sort(colConditions)

        ans = [[0] * k for _ in range(k)]
        for i in range(1, k+1):
            if i not in rows or i not in cols:
                return []
            if ans[rows[i]][cols[i]] != 0:
                return []
            ans[rows[i]][cols[i]] = i
        return ans


    
# @lc code=end

