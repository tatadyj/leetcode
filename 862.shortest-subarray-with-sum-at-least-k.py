#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] + nums
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]

        res = float('inf')
        queue = deque()
        for i in range(len(prefix_sum)):
            while queue and prefix_sum[queue[-1]] >= prefix_sum[i]:
                queue.pop()
            queue.append(i)

            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                res = min(res, i-queue[0])
                queue.popleft()
            
        return res if res != float('inf') else -1
# @lc code=end

