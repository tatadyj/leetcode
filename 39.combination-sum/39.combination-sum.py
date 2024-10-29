#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
def bt(ans, path, candidates, target, start):
    total = sum(path)
    if total > target:
        return 
    if total == target:
        ans.append(path[:])
        return 
    
    for i in range(start, len(candidates)):
        path.append(candidates[i])
        bt(ans, path, candidates, target, i)
        path.pop() 


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, path = [], []
        bt(ans, path, candidates, target, 0)
        return ans 
# @lc code=end

