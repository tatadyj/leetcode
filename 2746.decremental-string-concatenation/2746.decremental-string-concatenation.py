#
# @lc app=leetcode id=2746 lang=python3
#
# [2746] Decremental String Concatenation
#

# @lc code=start
class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        memo = [[[None]*26 for _ in range(26)] for _ in range(len(words))]
        def dfs(i, start, end):
            if i == len(words):
                return 0

            if memo[i][ord(start)-ord('a')][ord(end)-ord('b')] is not None:
                return memo[i][ord(start)-ord('a')][ord(end)-ord('b')]

            next_start, next_end = words[i][0], words[i][-1]
            # put front
            if next_end == start:
                front = len(words[i]) - 1 + dfs(i+1, next_start, end)
            else:
                front = len(words[i]) + dfs(i+1, next_start, end)
            # put back
            if end == next_start:
                back = len(words[i]) - 1 + dfs(i+1, start, next_end)
            else:
                back = len(words[i]) + dfs(i+1, start, next_end)
            
            ret = min(front, back)
            memo[i][ord(start)-ord('a')][ord(end)-ord('b')] = ret
            return ret
              
        return len(words[0]) + dfs(1, words[0][0], words[0][-1])
# @lc code=end

