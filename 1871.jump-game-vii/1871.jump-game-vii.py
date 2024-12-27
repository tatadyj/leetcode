#
# @lc app=leetcode id=1871 lang=python3
#
# [1871] Jump Game VII
#

# @lc code=start
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        '''
        此题是双臂区间 [i+minJump, i+maxJump]
        在 i+minJump    +1 
        在 i+maxJump+1  -1
        '''
        if s[-1] == '1': return False 

        n = len(s)
        diff = [0] * (n+1) # +1 due to []
        diff[minJump] += 1
        diff[maxJump + 1] -= 1

        count = 0 
        for i in range(1, n):
            count += diff[i]
            if s[i] == '1': continue 
            if count == 0: continue 

            if i + minJump <= n:
                diff[i + minJump] += 1

            if i + maxJump + 1 <= n:
                diff[i + maxJump + 1] -= 1
        
        return True if count != 0 else False
              
# @lc code=end

