#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        n = len(s)
        memo = [None] * 301 # 失败的例子

        def dfs(start):
            if memo[start] is not None:
                return memo[start]

            if start == n:
                return True
                
            curr = trie.root
            for i in range(start, n):
                if s[i] in curr.children:
                    curr = curr.children[s[i]]
                    if curr.is_end and dfs(i+1):
                        return True 
                else:
                    break 
            memo[start] = False
            return False 


        return dfs(0)

# @lc code=end

