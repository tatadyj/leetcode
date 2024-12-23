#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
class TrieNode:
    def __init__(self, char=''):
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
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        '''
        trie = Trie()
        for word in products:
            trie.insert(word)

        def dfs(curr, string):
            if len(ans) == 3:
                return 

            if curr.is_end:
                ans.append(string)

            for child in sorted(curr.children):
                dfs(curr.children[child], string+child)
            
        res = []
        curr = trie.root
        prefix = ''
        for i in range(len(searchWord)):
            prefix += searchWord[i]
            if searchWord[i] not in curr.children:
                for j in range(i, len(searchWord)):
                    res.append([])
                break
            curr = curr.children[searchWord[i]]

            # DFS for the current prefix
            start_node = curr
            ans = []
            dfs(start_node, '')
            for i in range(len(ans)):
                ans[i] = prefix + ans[i]
            res.append(ans)
        return res
        '''

        products.sort()
        res, prefix, i = [], '', 0
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, lo=i) # all the element before i not satisfied 
            res.append([w for w in products[i:i+3] if w.startswith(prefix)])
        return res

            
# @lc code=end

