#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#

# @lc code=start
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:   
        
        def count_less_or_equal(arr, val):
            count = 0
            max_frac = 0
            left_frac, right_frac = None, None
            target_i, target_j = None, None 
            l = 0
            r = 1 
            while l < len(arr):
                while r < len(arr) and arr[l]/arr[r] > val:
                    r += 1
                count += len(arr) - r 
                if r == len(arr):
                    break 

                if max_frac < arr[l]/arr[r]:
                    max_frac = arr[l]/arr[r]
                    left_frac = arr[l]
                    right_frac = arr[r]

                l += 1
            return count, left_frac, right_frac


        left, right = arr[0]/arr[-1], 1
        while left < right:
            mid = (left + right) / 2 # not //
            count, left_frac, right_frac = count_less_or_equal(arr, mid)
            if count == k:
                return [left_frac, right_frac]
            elif count > k:
                right = mid 
            else:
                left = mid 

        return []
    
        
# @lc code=end

