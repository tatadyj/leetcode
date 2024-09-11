#
# @lc app=leetcode id=1263 lang=python3
#
# [1263] Minimum Moves to Move a Box to Their Target Location
#

# @lc code=start
from collections import deque


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        queue = deque()
        visited = set()

        queue.append(start)
        visited.add(start)

        while queue: 
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()

                
# @lc code=end

