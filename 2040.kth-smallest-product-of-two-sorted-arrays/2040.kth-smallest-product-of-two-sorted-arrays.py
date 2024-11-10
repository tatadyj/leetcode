#
# @lc app=leetcode id=2040 lang=python3
#
# [2040] Kth Smallest Product of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_less_or_equal(nums1, nums2, val):
            count = 0 
            if val >= 0:
                j1, j2 = len(nums2) - 1, len(nums2) - 1
                for i in range(len(nums1)):
                    if nums1[i] == 0:
                        count += len(nums2)
                    elif nums1[i] > 0:
                        while j1 >= 0 and nums1[i] * nums2[j1] > val:
                            j1 -= 1 
                        count += j1 + 1
                    else: # nums[i] < 0
                        while j2 >= 0 and nums1[i] * nums2[j2] <= val:
                            j2 -= 1
                        count += len(nums2)-1 - (j2+1) + 1
            if val < 0:
                j1, j2 = 0, 0
                for i in range(len(nums1)):
                    if nums1[i] == 0:
                        continue 
                    elif nums1[i] > 0:
                        while j1 < len(nums2) and nums1[i] * nums2[j1] <= val:
                            j1 += 1 
                        count += (j1-1)-0+1 
                    else:
                        while j2 < len(nums2) and nums1[i] * nums2[j2] > val:
                            j2 += 1 
                        count += len(nums2)-1 - j2+1
            return count
        
        
        boundary = [nums1[0]*nums2[0], nums1[0]*nums2[-1], nums1[-1]*nums2[0], nums1[-1]*nums2[-1]]
        left, right = min(boundary), max(boundary)
        while left < right:
            mid = (left + right) // 2
            if count_less_or_equal(nums1, nums2, mid) < k:
                left = mid + 1 
            else:
                right = mid 
        return left 
        
# @lc code=end

