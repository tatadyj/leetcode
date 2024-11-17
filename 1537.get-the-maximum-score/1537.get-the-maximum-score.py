#
# @lc app=leetcode id=1537 lang=python3
#
# [1537] Get the Maximum Score
#

# @lc code=start
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0 
        m, n = len(nums1), len(nums2)
        x, y = 0, 0

        while i < m or j < n:
            if i == m:
                y += nums2[j]
                j += 1
            elif j == n:
                x += nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                x += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                y += nums2[j]
                j += 1
            else:
                x = max(x, y) + nums1[i]
                y = x
                i += 1
                j += 1
        
        return max(x, y) % (10**9 + 7)
# @lc code=end

