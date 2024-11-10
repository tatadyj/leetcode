#
# @lc app=leetcode id=1762 lang=python3
#
# [1762] Buildings With an Ocean View
#

# @lc code=start
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()

            stack.append(i)
        return stack
        
# @lc code=end

