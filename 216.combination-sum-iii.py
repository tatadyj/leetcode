#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start

def bt(ans, path, k, n, total, start):
    if total > n: return
    if len(path) == k and total == n:
        ans.append(path[:])
        return

    for i in range(start, 9-(k-len(path))+2):
        path.append(i)
        total += i
        bt(ans, path, k, n, total, i+1)
        total -= i            
        path.pop()



class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans, path = [], []
        bt(ans, path, k, n, 0, 1)
        return ans
        
# @lc code=end

