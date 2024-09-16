#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
            
            if stack[-1][1] == k:
                stack[-1][1] -= k
            if stack[-1][1] == 0:
                stack.pop()
    
        res = []
        for e in stack:
            res.extend([e[0]]*e[1])
        return ''.join(res)
                        
# @lc code=end

