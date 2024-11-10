#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List

def isPalindrome(substring):
    start, end = 0, len(substring)-1
    while start < end:
        if substring[start] != substring[end]:
            return False
        start += 1
        end -= 1
    return True

def bt(ans, substrings, s):
    if len(s) == 0:
        ans.append(substrings[:])
        return 

    for i in range(len(s)):
        if isPalindrome(s[0:i+1]):
            substrings.append(s[0:i+1])
        else:
            continue

        bt(ans, substrings, s[i+1:])
        substrings.pop()


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, substrings = [], []
        bt(ans, substrings, s)
        return ans
        

s = Solution()
print(s.partition("aabb"))
# @lc code=end

