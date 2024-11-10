#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        def partition(l, r, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            
            # 2. move all smaller elements to the left
            i = l 
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            # 3. move pivot to its final plance 
            nums[r], nums[i] = nums[i], nums[r]
            return i 
    
        def select(l, r, k):
            if l == r:      # list contains only one element
                return nums[l]

            # select a random pivot_index 
            p = random.randint(l, r)

            # find the pivot position in a sorted list
            p = partition(l, r, p)

            if p == k:
                return nums[p] 
            elif p < k:
                return select(p+1, r, k)
            else:
                return select(l, p-1, k)

        return select(0, len(nums)-1, len(nums)-k)
        '''

        #return heapq.nlargest(k, nums)[-1]
        # n*logC
        def count_larger_or_equal(val):
            count = 0
            for n in nums:
                if n >= val:
                    count += 1
            return count 

        left = min(nums)
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if count_larger_or_equal(mid) >= k:
                left = mid + 1
            else: # < k
                right = mid - 1
        return right
        
# @lc code=end

