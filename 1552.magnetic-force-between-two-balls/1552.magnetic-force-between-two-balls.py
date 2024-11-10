#
# @lc app=leetcode id=1552 lang=python3
#
# [1552] Magnetic Force Between Two Balls
#

# @lc code=start
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def is_valid(val):
            low = position[0]
            count = 1 
            for i in range(1, len(position)):
                if position[i] - low >= val:
                    count += 1 
                    low = position[i]
                if count >= m:
                    return True 
            return False 
        
        left, right = 1, position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2
            if is_valid(mid):
                left = mid
            else:
                right = mid - 1
        return left

# @lc code=end

