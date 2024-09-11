#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #res = heapq.nlargest(2, nums)
        #return (res[0]-1)*(res[1]-1)

        m = n = 0

        for num in nums:
            if num >= m and num > n:
                n = m
                m = num 
            if num < m and num > n:
                n = num 

        return (m-1) * (n-1)

# @lc code=end

