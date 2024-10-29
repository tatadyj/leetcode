#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start

def bt(ans, combination, k, n, start):
    if len(combination) == k:
        ans.append(combination.copy())
        return
    # 减枝
    # end = n - (k - len(combination)) + 2
    end = n + 1
    for i in range(start, end):
        combination.append(i)
        bt(ans, combination, k, n, i+1)
        combination.pop()


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, combination = [], []
        bt(ans, combination, k, n, 1)
        return ans

# @lc code=end

