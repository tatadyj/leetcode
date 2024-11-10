#
# @lc app=leetcode id=2115 lang=python3
#
# [2115] Find All Possible Recipes from Given Supplies
#

# @lc code=start
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj_dict = defaultdict(list)
        in_degree = defaultdict(int)
        for i in range(len(recipes)):
            for ing in ingredients[i]:
                adj_dict[ing].append(recipes[i])
                in_degree[recipes[i]] += 1

        queue = deque()
        for sup in supplies:
            queue.append(sup)

        while queue:
            curr = queue.popleft()
            for nxt in adj_dict[curr]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)

        ans = []
        for key in in_degree:
            if in_degree[key] == 0:
                ans.append(key)
        return ans       
# @lc code=end

