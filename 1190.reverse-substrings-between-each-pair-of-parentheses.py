#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        open = []
        pair = {}
        for i,c in enumerate(s):
            if c == '(':
                open.append(i)
            if c == ')':
                j = open.pop()
                pair[i] = j
                pair[j] = i 

        res = []
        i = 0 
        incr = 1
        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                incr = -incr
            else:
                res.append(s[i])
            i += incr
        return ''.join(res)        
# @lc code=end

