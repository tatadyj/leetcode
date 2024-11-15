#
# @lc app=leetcode id=2861 lang=python3
#
# [2861] Maximum Number of Alloys
#

# @lc code=start
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def is_ok(num):
            min_cost = inf 
            for i in range(len(composition)):
                total_cost = 0
                for j in range(len(composition[i])):
                    required = num * composition[i][j]
                    if stock[j] >= required:
                        continue
                    extra_cost = (required - stock[j]) * cost[j] 
                    total_cost += extra_cost
                min_cost = min(min_cost, total_cost)
            return min_cost <= budget

        left, right = 0,  10**9
        while left < right:
            mid = (left + right + 1) // 2
            if is_ok(mid):
                left = mid 
            else:
                right = mid - 1
        return left
# @lc code=end

