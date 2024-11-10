#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n 
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid): # bad
                right = mid
            else: # good
                left = mid + 1
        return left
        
# @lc code=end

