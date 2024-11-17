#
# @lc app=leetcode id=3048 lang=python3
#
# [3048] Earliest Second to Mark Indices I
#

# @lc code=start
class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        nums.insert(0, 0)
        changeIndices.insert(0, 0)
        n = len(nums)
        m = len(changeIndices)
        
        def is_ok(t):
            last = [0] * n
            for i in range(1, t+1):
                last[changeIndices[i]] = i

            for i in range(1, n):
                if last[i] == 0:
                    return False

            count = 0 
            for i in range(1, t+1):
                if i != last[changeIndices[i]]:
                    count += 1
                else:
                    count -= nums[changeIndices[i]]
                    if count < 0:
                        return False 
            return True 

        left = 1 
        right = m - 1

        while left < right:
            mid = (left + right) // 2 
            if is_ok(mid):
                right = mid 
            else:
                left = mid + 1
        if is_ok(left):
            return left 
        else:
            return - 1   
# @lc code=end

