#
# @lc app=leetcode id=1203 lang=python3
#
# [1203] Sort Items by Groups Respecting Dependencies
#

# @lc code=start
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        g = m
        for i in range(n):
            if group[i] == -1:
                group[i] = g
                g += 1

        graph = defaultdict(list)
        in_degree = [0] * n

        group_graph = defaultdict(list)
        group_in_degree = [0] * g

        for i in range(n):
            for j in beforeItems[i]:
                graph[j].append(i)
                in_degree[i] += 1
                if group[i] != group[j]:
                    if group[i] not in group_graph[group[j]]:
                        group_graph[group[j]].append(group[i])
                        group_in_degree[group[i]] += 1

        def topo_sort(in_degree, graph, n):
            queue = deque()
            for i in range(n):
                if in_degree[i] == 0:
                    queue.append(i)
        
            res = []
            while queue:
                curr = queue.popleft()
                res.append(curr)
                for nxt in graph[curr]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        queue.append(nxt)
            if len(res) != len(in_degree):
                return []
            else:
                return res

        item_order = topo_sort(in_degree, graph, n)
        if item_order == []:
            return []

        group_order = topo_sort(group_in_degree, group_graph, g)
        if group_order == []:
            return []

        ans = defaultdict(list)
        for item in item_order:
            ans[group[item]].append(item)

        ret = []
        for group_id in group_order:
            ret.extend(ans[group_id])
        return ret       
# @lc code=end

