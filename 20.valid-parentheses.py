#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

def use_dict(s):
    stack = []
    dict = {'(':')', '{':'}', '[':']'}
    for item in s:
        if item in dict:
            stack.append(dict[item])
        elif not stack or item != stack[-1]:
            return False 
        else:
            stack.pop()
                
    return not stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item =='{':
                stack.append('}')
            elif not stack or 
        
# @lc code=end

