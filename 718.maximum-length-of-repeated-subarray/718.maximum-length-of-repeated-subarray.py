#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1)+1, len(nums2)+1
        res = 0
        dp =[[0 for _ in range(len1)] for _ in range(len2)]
        for i in range(1, len2):
            for j in range(1, len1):
                if nums1[j-1] == nums2[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
        return res

# @lc code=end

