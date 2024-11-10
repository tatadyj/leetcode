#
# @lc app=leetcode id=2071 lang=python3
#
# [2071] Maximum Number of Tasks You Can Assign
#

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def is_ok(k, pills):
            sl = SortedList(workers[-k:])
          
            for task in tasks[:k][::-1]:
                idx = sl.bisect_left(task) #找那个刚好能胜任的人
                if idx < len(sl):
                    sl.pop(idx)
                elif pills > 0:
                    idx = sl.bisect_left(task - strength)
                    if idx < len(sl):
                        sl.pop(idx)
                        pills -= 1
                else:
                    return False 
            return len(sl) == 0


        left = 0 
        right = min(len(tasks), len(workers)) 
        while left < right:
            mid = (left + right + 1) // 2
            if is_ok(mid, pills):
                left = mid 
            else:
                right = mid - 1
        return left

        
# @lc code=end

