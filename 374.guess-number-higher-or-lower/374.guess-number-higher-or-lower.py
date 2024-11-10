#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n 

        while left < right - 1:
            mid = (left + right) // 2
            cond = guess(mid)
            if cond == 1:
                left = mid
            elif cond == -1:
                right = mid
            else:
                return mid 
                
        return left if guess(left) == 0 else right


# @lc code=end

