#
# @lc app=leetcode id=1201 lang=python3
#
# [1201] Ugly Number III
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def count_less_or_equal(val):
            return val//a + val//b + val//c - val//math.lcm(a, b) - val//math.lcm(b, c) - val//math.lcm(a,c) + val//math.lcm(math.lcm(a,b),c)


        left = 1
        right = 10**18
        while left < right:
            mid = (left + right) // 2
            if count_less_or_equal(mid) >= n:
                right = mid 
            else:
                left = mid + 1
        return left      
# @lc code=end

