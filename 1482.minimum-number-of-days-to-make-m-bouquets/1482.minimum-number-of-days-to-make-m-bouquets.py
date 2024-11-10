#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return - 1
        min_val = min(bloomDay)
        max_val = max(bloomDay)

        def is_valid(val):
            # 在第val天，有没有m个连续的k滑窗
            num_of_bq = 0
            count = 0 

            for day in bloomDay:
                if day <= val:
                    count += 1 
                else:
                    count = 0 

                if count == k:
                    num_of_bq += 1 
                    count = 0 
            return num_of_bq >= m
            
        left, right = min_val, max_val
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1 
        if is_valid(left):
            return left
        else:
            return -1
# @lc code=end

