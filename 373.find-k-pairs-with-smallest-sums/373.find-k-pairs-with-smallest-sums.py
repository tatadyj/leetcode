#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def count_less_or_equal(val):
            count = 0
            j = len(nums2) - 1 
            for i in range(len(nums1)):
                while j >= 0 and nums1[i] + nums2[j] > val:
                    j -= 1
                count += j + 1
            return count
            
        left = nums1[0] + nums2[0]
        right = nums1[-1] + nums2[-1]

        while left < right:
            mid = (left + right) // 2
            count = count_less_or_equal(mid)
            if count >= k:
                right = mid 
            else:
                left = mid + 1
        thr = left
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] + nums2[j] < thr:
                    res.append((nums1[i], nums2[j]))
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] + nums2[j] == thr and len(res) < k:
                    res.append((nums1[i], nums2[j]))
        return res

            
        
# @lc code=end

