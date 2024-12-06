#
# @lc app=leetcode id=425 lang=python3
#
# [425] Word Squares
#

# @lc code=start
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        ans = []
        square = ['' for _ in range(n)]
        prefix = defaultdict(set)

        for word in words:
            for i in range(n):
                prefix[word[:i]].add(word)
  
        def dfs(row):
            if row == n:
                ans.append(square[:])
                return 

            prefix_key = []
            for i in range(0, row):
                prefix_key.append(square[i][row])
            prefix_key = ''.join(prefix_key)
            for word in prefix[prefix_key]:
                square[row] = word
                dfs(row+1)
                square[row] = ''

        dfs(0)
        return ans 


# @lc code=end

