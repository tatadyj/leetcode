#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#

# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        diff = [0] * (n+1)

        for i in range(n):
            start, end = 0, i+1
            diff[start] += shifts[i]
            diff[end] -= shifts[i]

        sum = 0 
        s = list(s)
        for i in range(n):
            sum += diff[i]
            s[i] = chr(ord('a') + (ord(s[i]) - ord('a') + sum) % 26)

        return ''.join(s) 
# @lc code=end

