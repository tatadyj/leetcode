#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def bt(curr_str, left, right):
            if len(curr_str) == 2*n:
                ans.append(curr_str)
                return 

            if left < n:
                bt(curr_str + "(", left+1, right)
            if right < left:
                bt(curr_str + ")", left, right+1)

        ans = []
        bt("", 0, 0) # number of left and right 
        return ans
        
# @lc code=end

