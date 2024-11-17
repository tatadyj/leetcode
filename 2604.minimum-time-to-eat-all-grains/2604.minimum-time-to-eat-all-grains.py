#
# @lc app=leetcode id=2604 lang=python3
#
# [2604] Minimum Time to Eat All Grains
#

# @lc code=start
class Solution:
    def minimumTime(self, hens: List[int], grains: List[int]) -> int:
        hens.sort()
        grains.sort()
        def is_ok(time):
            j = 0
            for i in range(len(hens)):
                if grains[j] < hens[i]:
                    t = hens[i] - grains[j]
                    if t > time: return False 
                else:
                    t = 0 
                
                while j < len(grains) and grains[j] <= hens[i]:
                    j += 1

                if time - 2*t > (time - t) / 2:
                    while j < len(grains) and time - 2*t - (grains[j] - hens[i]) >= 0:
                        j += 1
                else:
                    while j < len(grains) and (time - t) /2 - (grains[j] - hens[i]) >= 0:
                        j += 1
                if j == len(grains): 
                    return True 
            return False



        left, right = 0, 2**31-1
        while left < right:
            mid = (left + right) // 2
            if is_ok(mid):
                right = mid 
            else:
                left = mid + 1
        return left 
# @lc code=end

