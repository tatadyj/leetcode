#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict = {}
        count = 0

        for n1 in nums1:
            for n2 in nums2:
                total = n1 + n2
                if total in dict:
                    dict[total] += 1
                else:
                    dict[total] = 1

        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                if key in dict:
                    count += dict[key]
                    
        return count
# @lc code=end

