#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
from typing import List 

def bt(ans, path, wordDict, minSize, s):
    if len(s) == 0:
        ans.append(' '.join(path))
        return 

    for i in range(minSize-1, len(s)):
        if s[0:i+1] in wordDict:
            path.append(s[0:i+1])
        else:
            continue
                
        bt(ans, path, wordDict, minSize, s[i+1:])
        path.pop()



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans, path = [], []
        memo = {}

        # prune
        minSize = min([len(w) for w in wordDict])
        wordDict = set(wordDict)
        bt(ans, path, wordDict, minSize, s)
        return ans
        
print(Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))

# @lc code=end

