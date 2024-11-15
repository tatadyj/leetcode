#
# @lc app=leetcode id=793 lang=python3
#
# [793] Preimage Size of Factorial Zeroes Function
#

# @lc code=start
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailingZeros(n):
            res = 0 
            divisor = 5
            while divisor <= n:
                res += n // divisor
                divisor *= 5
            return res 
        
        def binary_search(target):
            # min val, left bound
            lo, hi = 0, 2**63 - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if trailingZeros(mid) >= target:
                    hi = mid 
                else:
                    lo = mid + 1
            return lo 

        return binary_search(k+1)-1 - binary_search(k) + 1
# @lc code=end

