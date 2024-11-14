#
# @lc app=leetcode id=878 lang=python3
#
# [878] Nth Magical Number
#

# @lc code=start
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def count_less_or_equal(val):
            return val//a + val//b - val//math.lcm(a,b)

        left = 2
        right = n * min(a, b)

        while left < right:
            mid = (left + right) // 2
            if count_less_or_equal(mid) >= n:
                right = mid 
            else:
                left = mid + 1
        return left % (10**9 + 7)
# @lc code=end

