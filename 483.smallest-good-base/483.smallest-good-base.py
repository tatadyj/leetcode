#
# @lc app=leetcode id=483 lang=python3
#
# [483] Smallest Good Base
#

# @lc code=start
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        """
        根据等比数列求和公式：(k^m - 1) / (k - 1) = n
        并且k越大，m越小。k取值范围[2, n-1]。 
        当k = n-1, m = 2; e.g. (n-1)^1 + (n-1)^0 = n
        当k = 2, m = int(log2(n+1))
        m的取值范围[2, int(log2(n+1))] = [2, 59]
        n最小是3，m最小是2
        """
        def compute(k, m):
            res = 0
            for i in range(m):
                res = res*k + 1
            return res

        n = int(n)
        for m in range(59, 1, -1):
            # binary search of k
            left = 2
            right = n-1
            while left < right:
                mid = (left + right) // 2
                val = compute(mid,  m)
                if val >= n:
                    right = mid 
                else:
                    left = mid + 1 
            if compute(left, m) == n:
                return str(left) 

# @lc code=end

