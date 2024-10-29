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
        # 维护单调递减栈，一旦右边比左边高，左边只能看到右边这一个
        # 所以左边退栈，看到个数+1
        # 单调递减都能看到右边+1
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                j = stack.pop()
                res[j] += 1
            if stack:
               res[stack[-1]] += 1
            stack.append(i)

        return res

# @lc code=end

