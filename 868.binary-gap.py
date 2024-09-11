#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)
        if binary.count('1') < 2:
            return 0 
        

        
# @lc code=end

