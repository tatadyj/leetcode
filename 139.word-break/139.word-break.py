#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from typing import List 

def bt(wordDict, minSize, memo, s):
    if len(s) == 0:
        return True

    if s in memo:
        return memo[s]

    for i in range(minSize-1, len(s)):
        substring = s[0:i+1]
        if substring in wordDict:
            ret = bt(wordDict, minSize, memo, s[i+1:])
            if ret:
                return True

    memo[s] = False 
    return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        minSize = min([len(w) for w in wordDict])
        wordDict = set(wordDict)
        return bt(wordDict, minSize, memo, s)

print(Solution().wordBreak("aaaaaaaa", ["aaa", "aaaa"]))
# @lc code=end

