#
# @lc app=leetcode id=798 lang=python3
#
# [798] Smallest Rotation with Highest Score
#

# @lc code=start
class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        '''
        nums[i] <= i 
        0123456
            2            
        0011111 -> 1110011
        diff[0] += 1
        diff[i-(nums[i]-1)] -= 1
        diff[i+1] += 1

        nums[i] > i
        0123456
          4
        0000111 -> 001110
        diff[0] += 0
        diff[i+1] += 1
        diff[i+1+(n-nums[i])] -= 1
        '''
        n = len(nums)
        diff = [0] * n 

        for i in range(n):
            if nums[i] <= i:
                diff[0] += 1
                diff[( i-(nums[i]-1) ) % n] -= 1
                diff[(i+1) % n] += 1
            else:
                diff[0] += 0
                diff[(i+1) % n] += 1
                diff[( i+1+(n-nums[i]) ) % n] -= 1

        max_score = 0
        score = 0
        ret = 0
        for i in range(n):
            score += diff[i]
            if score > max_score:
                max_score = score 
                ret = i

        return ret
                
# @lc code=end

