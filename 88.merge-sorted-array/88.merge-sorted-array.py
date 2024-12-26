#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
def forward():
        p1 = p2 = 0
        nums1_copy = nums1[:m].copy()

        for p in range(m+n):
            if p1 < m and p2 < n:
                if nums1_copy[p1] < nums2[p2]:
                    nums1[p] = nums1_copy[p1]
                    p1 += 1
                else:
                    nums1[p] = nums2[p2]
                    p2 += 1
            else:
                if p1 < m:
                    nums1[p] = nums1_copy[p1]
                    p1 += 1

                if p2 < n:
                    nums1[p] = nums2[p2]
                    p2 += 1 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1 

        for p in range(m+n-1, -1, -1):
            if p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[p] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[p] = nums2[p2]
                    p2 -= 1
            else:
                if p2 >= 0:
                    nums1[p] = nums2[p2]
                    p2 -= 1

        
# @lc code=end

