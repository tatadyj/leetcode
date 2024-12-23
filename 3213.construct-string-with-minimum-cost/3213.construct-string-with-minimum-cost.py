#
# @lc app=leetcode id=3213 lang=python3
#
# [3213] Construct String with Minimum Cost
#

# @lc code=start
class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.cost = -1 
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, cost):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        if curr.cost == -1:
            curr.cost = cost 
        else:
            curr.cost = min(curr.cost, cost)

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(word, costs[i])

        memo = [None] * len(target)
        def dfs(start):
            if start == len(target):
                return 0

            if memo[start] is not None:
                return memo[start]


            res = inf
            curr = trie.root
            for i in range(start, len(target)):
                if target[i] not in curr.children: break 
                curr = curr.children[target[i]]
                if curr.cost != -1:
                    res = min(res, dfs(i+1) + curr.cost)
            
            memo[start] = res
            return res 
           
        ret = dfs(0)
        if ret == inf: 
            return -1 
        else:
            return ret
# @lc code=end

