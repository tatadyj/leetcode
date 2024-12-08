#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
def is_palindrome(substring):
    start, end = 0, len(substring) - 1
    while start < end:
        if substring[start] != substring[end]:
            return False 
        start += 1 
        end -= 1
    return True

def bt(ans, path, s):
    if len(s) == 0:
        ans.append(path.copy())
        return 

    for i in range(len(s)):
        if is_palindrome(s[:i+1]): #[0, i]
            path.append(s[:i+1])
            bt(ans, path, s[i+1:])
            path.pop()


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, path = [], []
        bt(ans, path, s)
        return ans 

# @lc code=end

