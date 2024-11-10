#
# @lc app=leetcode id=2030 lang=python3
#
# [2030] Smallest K-Length Subsequence With Occurrences of a Letter
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        stack = []
        num_removed = len(s) - k
        count = 0
        for c in s:
            if c == letter:
                count += 1

        for i in range(len(s)):
            while stack and s[stack[-1]] > s[i] and num_removed > 0:
                if s[stack[-1]] != letter: 
                    stack.pop()
                    num_removed -= 1
                else:
                    if count-1 >= repetition:
                        stack.pop()
                        num_removed -= 1
                        count -= 1
                    else:
                        break 
            stack.append(i)

        keep = []
        while num_removed > 0:
            if s[stack[-1]] != letter: 
                stack.pop()
                num_removed -= 1
            else:
                if count-1 >= repetition:
                    stack.pop()
                    num_removed -= 1 
                    count -= 1 
                else:
                    keep.append(stack.pop())
        
        return ''.join([s[i] for i in stack+keep])        
# @lc code=end

