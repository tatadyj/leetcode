#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def count_missing(val):
            # count # of missing for mid - 1
            # we don't know whether mid is missing or not 
            idx = bisect.bisect_left(arr, val) # count how many element in the arr and <= mid-1
            return val-1 - idx


        left = 1 
        right = max(arr) + k 

        while left < right:
            mid = (left + right + 1) // 2
            count = count_missing(mid)
            if count < k - 1:
                left = mid + 1
            elif count > k - 1:
                right = mid - 1
            else:
                left = mid
        return left
        
        
# @lc code=end

