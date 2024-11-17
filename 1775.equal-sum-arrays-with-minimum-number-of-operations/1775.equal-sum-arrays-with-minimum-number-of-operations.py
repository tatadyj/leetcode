#
# @lc app=leetcode id=1775 lang=python3
#
# [1775] Equal Sum Arrays With Minimum Number of Operations
#

# @lc code=start
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        nums1.sort(reverse=True)
        nums2.sort()
        if sum1 < sum2:
            nums1, nums2 = nums2, nums1

        # sum1 > sum2
        count = 0 
        i = 0
        j = 0 
        while (i < len(nums1) or j < len(nums2)) and (sum1 > sum2):
            d1, d2 = None, None
            if i < len(nums1):
                d1 = nums1[i] - 1
            if j < len(nums2):
                d2 = 6 - nums2[j]
    
            if d1 and d2:
                if d1 >= d2:
                    sum1 -= d1 
                    count += 1
                    i += 1
                else:
                    sum2 += d2
                    count += 1
                    j += 1
            elif d1:
                sum1 -= d1 
                count += 1
                i += 1
            elif d2:
                sum2 += d2
                count += 1
                j += 1
            else:
                return -1 
        return count
# @lc code=end

