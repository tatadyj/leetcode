#
# @lc app=leetcode id=1593 lang=python3
#
# [1593] Split a String Into the Max Number of Unique Substrings
#

# @lc code=start
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        used = set()
        res = 1
        def dfs(start, count):
            nonlocal res
            if start == n:
                res = max(res, count)
                return

            if count + n - start <= res:
                return

            for i in range(start, n):
                if s[start:i+1] not in used:
                    used.add(s[start:i+1])
                    dfs(i+1, count+1)
                    used.remove(s[start:i+1])

        dfs(0, 0)
        return res
# @lc code=end

