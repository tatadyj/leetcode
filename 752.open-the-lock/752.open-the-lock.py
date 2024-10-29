#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deadends = set(deadends)
        queue = deque()
        visited = set()
        start = '0000'
        queue.append(start)
        visited.add(start)
        
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_str = queue.popleft()
                if curr_str in deadends:
                    continue
                if curr_str == target:
                    return step 

                for i in range(len(target)):
                    for j in [1, -1]:
                        curr = list(curr_str)
                        curr[i] = str((int(curr[i]) + j) % 10)    
                        temp_str = ''.join(curr)
                        
                        if temp_str not in visited:
                            visited.add(temp_str)
                            queue.append(temp_str)
            step += 1
        return -1
        
# @lc code=end

