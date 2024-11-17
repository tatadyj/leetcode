#
# @lc app=leetcode id=1229 lang=python3
#
# [1229] Meeting Scheduler
#

# @lc code=start
def two_pointer():
    slots1.sort()
    slots2.sort()

    i = 0 
    j = 0 
    while i < len(slots1) and j < len(slots2):
        a = slots1[i]
        b = slots2[j]
        start = max(a[0], b[0])
        end = min(a[1], b[1])
        if end - start >= duration:
            return [start, start+duration]
        else:
            if a[1] < b[1]:
                i += 1
            else:
                j += 1
    return []

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # 差分数组
        arr = []
        for s in slots1 + slots2:
            arr.append((s[0], 1))
            arr.append((s[1], -1))
        arr.sort()
        count = 0
        start = None
        for i in range(len(arr)):
            count += arr[i][1]
            if count == 2:
                start = arr[i][0]
            if start is not None and count == 1:
                if arr[i][0] - start >= duration:
                    return [start, start+duration]
                else:
                    start = None
        return []

            
# @lc code=end

