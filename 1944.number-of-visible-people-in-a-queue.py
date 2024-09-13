#
# @lc app=leetcode id=1944 lang=python3
#
# [1944] Number of Visible People in a Queue
#

# @lc code=start
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0] * len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                j = stack.pop()
                res[j] += 1 

            if stack:
                res[stack[-1]] += 1

            stack.append(i)

        return res


# @lc code=end

