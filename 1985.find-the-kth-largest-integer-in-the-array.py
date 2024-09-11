#
# @lc app=leetcode id=1985 lang=python3
#
# [1985] Find the Kth Largest Integer in the Array
#

# @lc code=start
import random
from typing import List 

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(n) for n in nums]
        random.shuffle(nums)
        def partition(l, r, p):
            pivot = nums[p]
            nums[p], nums[r] = nums[r], nums[p]
            i = l 
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i 

        def select(l, r, k):
            if l == r:
                return nums[l]
            p = random.randint(l, r)
            p = partition(l, r, p)

            if p == k:
                return nums[k]
            elif p < k:
                return select(p+1, r, k)
            else:
                return select(l, p-1, k)

        return str(select(0, len(nums)-1, len(nums)-k))

Solution().kthLargestNumber(["3","6","7","10"],4)
# @lc code=end

