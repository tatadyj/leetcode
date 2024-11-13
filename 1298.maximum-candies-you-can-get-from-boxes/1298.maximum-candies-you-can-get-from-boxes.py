#
# @lc app=leetcode id=1298 lang=python3
#
# [1298] Maximum Candies You Can Get from Boxes
#

# @lc code=start
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        my_keys = set()
        queue = deque()
        count = 0
        for box in initialBoxes:
            queue.append(box)

        while queue:
            size = len(queue)
            at_least_one_open = False
            for _ in range(size):
                box = queue.popleft()
                if status[box] == 0 and box not in my_keys:
                    queue.append(box)
                else:
                    at_least_one_open = True
                    count += candies[box]
                    for key in keys[box]:
                        my_keys.add(key)
                    for nxt in containedBoxes[box]:
                        queue.append(nxt)
            if at_least_one_open == False:
                break
        return count
    
# @lc code=end

