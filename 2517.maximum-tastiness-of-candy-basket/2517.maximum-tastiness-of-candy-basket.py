#
# @lc app=leetcode id=2517 lang=python3
#
# [2517] Maximum Tastiness of Candy Basket
#

# @lc code=start
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def is_ok(min_val):
            count = 1
            i = 0 
            j = 1
            while j < len(price):
                if price[j] - price[i] >= min_val:
                    count += 1
                    i = j
                j += 1
                if count >= k:
                    return True 
            return count >= k

        left = 0
        right = price[-1] - price[0]
        while left < right:
            mid = (left + right + 1) // 2
            if is_ok(mid):
                left = mid 
            else:
                right = mid - 1
        return left 
# @lc code=end

