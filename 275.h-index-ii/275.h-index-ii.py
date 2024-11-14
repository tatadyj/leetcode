#
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)     
        left = 0 
        right = n - 1

        while left < right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid: # 引用数 >= 篇数， 符合定义但是不是最大篇数
                right = mid 
            else: # citations[mid] < n - mid 引用数 < 篇数 不符合定义
                left = mid + 1

        if citations[left] >= n - left:
            return n - left 
        else:
            return 0      
# @lc code=end

