#
# @lc app=leetcode id=1818 lang=python3
#
# [1818] Minimum Absolute Sum Difference
#

# @lc code=start
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        arr = nums1.copy()
        arr.sort()
        res = sum([abs(a-b) for a,b in zip(nums1, nums2)])

        min_val = 0
        for i in range(len(nums1)):
            diff = abs(nums1[i] - nums2[i])
            # find a* |a* - b| the smallest
            idx = bisect.bisect_left(arr, nums2[i])
            if idx < len(arr) and arr[idx] != nums1[i]:
                if abs(arr[idx] - nums2[i]) - diff < min_val:
                    min_val = abs(arr[idx] - nums2[i]) - diff
            
            if idx - 1 >= 0 and arr[idx - 1] != nums1[i]:
                if abs(arr[idx-1] - nums2[i]) - diff < min_val:
                    min_val = abs(arr[idx-1] - nums2[i]) - diff
          
        return (res + min_val) % (10**9 + 7)    
# @lc code=end

