#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums 

        res = []
        queue = deque()
        for i in range(k):
            while queue and nums[i] > queue[-1]:
                    queue.pop() 
            queue.append(nums[i])

        res.append(queue[0])
        for i in range(k, len(nums)):
            if nums[i-k] == queue[0]:
                queue.popleft()

            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
            
            res.append(queue[0])

        return res 


# @lc code=end

