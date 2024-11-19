#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#

# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0 
        window = defaultdict(int)
        max_freq = 0
        left = 0
        for right in range(len(answerKey)):
            rval = answerKey[right]
            window[rval] += 1
            max_freq = max(max_freq, window[rval])
            while right - left + 1 - max_freq > k:
                lval = answerKey[left]
                window[lval] -= 1 
                left += 1
            res = max(res, right - left + 1)
        return res  
# @lc code=end

