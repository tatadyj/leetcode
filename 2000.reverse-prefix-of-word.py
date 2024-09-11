#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)

        for i,c in enumerate(word):
            if c == ch:
                l, r = 0, i
                while l < r:
                    word[l], word[r] = word[r], word[l]
                    l += 1
                    r -= 1
                break  
        
        return ''.join(word)


        
# @lc code=end

