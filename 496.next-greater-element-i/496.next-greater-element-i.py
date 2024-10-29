#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from typing import List 

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        # 建立dict nums1 = [4, 1, 2]
        # map = {4:0, 1:1, 2:2}
        map = {v:i for i,v in enumerate(nums1)}
        stack = [0]

        for i in range(1, len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums2[i] > nums2[stack[-1]]:
                    j = stack.pop()
                    # 如果pop的元素也在nums1中， 提取它在nums1中的index
                    # 然后更新对应在res中的值
                    if nums2[j] in map:
                        res[map[nums2[j]]] = nums2[i]
                stack.append(i)

        return res 
Solution().nextGreaterElement([4,1,2],[1,3,4,2])
# @lc code=end

