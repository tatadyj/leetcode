#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#

# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1 = len(s1)
        l2 = len(s2)
        res = [[None]*(l2+1) for i in range(l1+1)]
        a1 = [ord(e) for e in s1]
        a2 = [ord(e) for e in s2]
        
        res[0][0] = 0
        for i in range(1, l1+1):
            res[i][0] = sum(a1[:i])
            
        for j in range(1, l2+1):
            res[0][j] = sum(a2[:j])
            
        for i in range(l1):
            for j in range(l2):
                if s1[i] == s2[j]:
                    res[i+1][j+1] = res[i][j]
                else:
                    res[i+1][j+1] = min(res[i][j+1]+a1[i], 
                                       res[i+1][j]+a2[j], 
                                       res[i][j]+a1[i]+a2[j])
                    
        return res[-1][-1]
                
# @lc code=end

