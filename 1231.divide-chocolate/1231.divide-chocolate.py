#
# @lc app=leetcode id=1231 lang=python3
#
# [1231] Divide Chocolate
#

# @lc code=start
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # 不能sort，因为巧克力是一整块连续的
        def is_ok(min_val):
            count = 0
            sum = 0
            for sw in sweetness:
                sum += sw
                if sum >= min_val:
                    count += 1 
                    sum = 0
            return count >= k + 1
                      

        left = min(sweetness)
        right = sum(sweetness) // (k + 1)
        while left < right:
            mid = (left + right + 1) // 2
            if is_ok(mid):
                left = mid 
            else:
                right = mid - 1
        return left
        
# @lc code=end

