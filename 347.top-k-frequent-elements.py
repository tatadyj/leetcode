#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List 
from collections import Counter 
import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        '''
        def partition(l, r, pivot_index):
            pivot = count[unique[pivot_index]]

            unique[pivot_index], unique[r] = unique[r], unique[pivot_index]

            i = l
            for j in range(l, r):
                if count[unique[j]] < pivot:
                    unique[j], unique[i] = unique[i], unique[j]
                    i += 1

            unique[r], unique[i] = unique[i], unique[r]
            return i 

        def quickselect(l, r, k):
            if l == r:
                return 

            p = random.randint(l, r)
            p = partition(l, r, p)
            if k == p:
                return 
            elif k < p:
                quickselect(l, p-1, k)
            else:
                quickselect(p+1, r, k)
            
        quickselect(0, len(unique)-1, len(unique)-k)
        return unique[len(unique)-k:]
        '''
        return heapq.nlargest(k, count.keys(), key=count.get)

Solution().topKFrequent([1,1,1,2,2,3], 2)
# @lc code=end

