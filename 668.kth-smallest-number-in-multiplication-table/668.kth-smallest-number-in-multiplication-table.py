#
# @lc app=leetcode id=668 lang=python3
#
# [668] Kth Smallest Number in Multiplication Table
#

# @lc code=start
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 1 
        right = m*n 

        def less_or_equal(val):
            count = 0 
            
            i = m
            j = 1
            while j <= n:
                if i*j <= val:
                    count += i
                    j += 1
                else:
                    i -= 1
            return count 



        while left < right:
            mid = (left + right) // 2
            count = less_or_equal(mid)
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left 
        
# @lc code=end

