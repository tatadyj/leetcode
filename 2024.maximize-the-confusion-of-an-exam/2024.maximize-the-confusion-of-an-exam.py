#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#

# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def sliding_window(char):
            res = 0 
       
            l = 0
            count = 0
            for r in range(len(answerKey)):
                rval = answerKey[r]
                if rval != char:
                    count += 1

                while l < len(answerKey) and count > k:
                    lval = answerKey[l]
                    if lval != char:
                        count -= 1
                    l += 1
                res = max(res, r-l+1)
            return res
        
        return max(sliding_window('T'), sliding_window('F'))
        
# @lc code=end

