#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
def use_stack(s):
    stack = []
    for item in s:
        if stack and item == stack[-1]:
            stack.pop()
        else:
            stack.append(item)
                
    return ''.join(stack)  

def use_two_pointers(s):
    sList = list(s)
    slow = fast = 0

    while fast < len(sList):
        if sList[slow] == sList[fast]:
            sList[slow] = sList[fast]
        else:
            slow += 1
        fast += 1
    return ''.join(sList[:slow])


class Solution:
    def removeDuplicates(self, s: str) -> str:
   
# @lc code=end

