#
# @lc app=leetcode id=2049 lang=python3
#
# [2049] Count Nodes With the Highest Score
#

# @lc code=start
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        adj_dict = defaultdict(list)
        for i in range(n):
            adj_dict[parents[i]].append(i)
        
        ans = defaultdict(int)
        def dfs(curr):
            count_list = sorted([dfs(child) for child in adj_dict[curr]])
            prod = 1
            for count in count_list:
                prod *= count 
            remain = n - sum(count_list) - 1
            if remain != 0:
                prod *= remain 

            ans[prod] += 1
            return sum(count_list) + 1
            

        dfs(0)
        max_score = max(ans.keys())
        return ans[max_score]
           
# @lc code=end

