#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.is_end = False 
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.is_end = True  

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        ans = []
        path = []
        memo = [None] * 301

        def dfs(start):
            if memo[start] is not None:
                return memo[start]

            if start == n:
                ans.append(' '.join(path))
                return True

            curr = trie.root
            flag = False
            for i in range(start, n):
                if s[i] in curr.children:
                    curr = curr.children[s[i]]
                    if curr.is_end:
                        path.append(s[start:i+1])
                        flag = dfs(i+1)
                        path.pop()
                else:
                    break
            if flag == False:
                memo[start] = flag
            return flag

        dfs(0)
        return ans
        
# @lc code=end

