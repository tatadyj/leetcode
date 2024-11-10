#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque()
        visited = set()

        queue.append(rooms[0])
        visited.add(rooms[0])

        while queue:
            size = len(queue)

            for _ in range(size):
                keys = queue.popleft()
                for key in keys:
                    new_keys = rooms[key]
                    for new_key in new_keys:
                        if new_key not in visited:
                            visited.add(new_key)
                            queue.append(new_key)


        
# @lc code=end

