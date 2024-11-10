#
# @lc app=leetcode id=418 lang=python3
#
# [418] Sentence Screen Fitting
#

# @lc code=start
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence =  ' '.join(sentence)
        sentence += ' '
        n = len(sentence)
        
        c = 0
        for r in range(rows):
            c += cols
            while sentence[c % n] != ' ':
                c -= 1
            c += 1 
        return c // n    
# @lc code=end

