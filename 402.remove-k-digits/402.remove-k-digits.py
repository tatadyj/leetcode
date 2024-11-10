#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [0]

        for i in range(1, len(num)):
            if num[i] >= num[stack[-1]]:
                stack.append(i)
            
            else:
                while stack and num[i] < num[stack[-1]] and k > 0:
                    stack.pop() 
                    k -= 1 
                stack.append(i)

        return "".join([num[i] for i in stack])            
        

        
# @lc code=end

