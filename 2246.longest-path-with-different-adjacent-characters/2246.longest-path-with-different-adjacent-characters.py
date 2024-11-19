#
# @lc app=leetcode id=2246 lang=python3
#
# [2246] Longest Path With Different Adjacent Characters
#

# @lc code=start
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj_dict = defaultdict(list)
        n = len(parent)
        for i in range(n):
            adj_dict[parent[i]].append(i)

        ans = 0
        def dfs(curr):
            nonlocal ans

            node_num_list = []
            for child in adj_dict[curr]:
                v = dfs(child)
                if s[child] != s[curr]:
                    node_num_list.append(v)
            node_num_list.sort(reverse=True)

            sum_node_num = 1
            if len(node_num_list) >= 2:
                sum_node_num += node_num_list[0] + node_num_list[1]

            if len(node_num_list) == 1:
                sum_node_num += node_num_list[0]

            max_node_num = 0
            if len(node_num_list) > 0:
                max_node_num = node_num_list[0]            

            ans = max(ans, sum_node_num)    
            return max_node_num + 1

        dfs(0)
        return ans

        
# @lc code=end

