#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
def bt(ans, path, candidates, target, start):
    if sum(path) > target:
        return 
    if sum(path) == target:
        ans.append(path.copy())
        return 
    
    for i in range(start, len(candidates)):
        if i-1 >= start and candidates[i-1] == candidates[i]: 
            continue 
        path.append(candidates[i])
        bt(ans, path, candidates, target, i+1)
        path.pop()

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, path = [], []
        candidates.sort()
        bt(ans, path, candidates, target, 0)
        return ans
        
# @lc code=end

