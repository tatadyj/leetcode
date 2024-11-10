#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(grumpy)
        sum = 0 
        for i in range(n):
            if grumpy[i] == 0:
                sum += customers[i]
        res = 0
        window_sum = 0
        left = 0 
        for right in range(n):
            rval = customers[right]
            window_sum += rval 
            if grumpy[right] == 0:
                sum -= rval  

            while right - left + 1 > minutes:
                lval = customers[left]
                window_sum -= lval
                if grumpy[left] == 0:
                    sum += lval 
                left += 1
            
            if right - left + 1 == minutes:
                res = max(res, sum+window_sum)
        return res
# @lc code=end

