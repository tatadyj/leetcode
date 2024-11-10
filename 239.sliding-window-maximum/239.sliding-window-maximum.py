#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()

        for i in range(len(nums)):
            window_start = i - k + 1
            # 窗口左边index: queue[0]
            # 当窗口左边的index越界
            # 假设i已经入队的情况
            while queue and queue[0] < window_start:
                queue.popleft()

            # 处理右边窗口，保证单调递减
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop() 

            queue.append(i)
            
            # 当窗口左边index >= 0开始记录窗口最大值
            # 并且每次移动i都要记录一次
            if window_start >= 0:
                res.append(nums[queue[0]])
                
        return res 



# @lc code=end

