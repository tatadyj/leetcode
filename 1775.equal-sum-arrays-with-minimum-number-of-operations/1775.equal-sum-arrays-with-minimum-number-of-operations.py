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
            return self.minOperations(nums2, nums1)

        # sum1 > sum2
        diff = sum1 - sum2
        count = 0 
        i = 0
        j = 0 
        while diff > 0:
            if i >= len(nums1) and j >= len(nums2):
                return - 1
            elif i < len(nums1) and j >= len(nums2):
                diff -= nums1[i] - 1
                i += 1
            elif j < len(nums2) and i >= len(nums1):
                diff -= 6 - nums2[j]
                j += 1
            else:
                d1 = nums1[i] - 1
                d2 = 6 - nums2[j]
                if d1 >= d2:
                    diff -= d1 
                    i += 1
                else:
                    diff -= d2
                    j += 1
            count += 1
        return count
# @lc code=end

