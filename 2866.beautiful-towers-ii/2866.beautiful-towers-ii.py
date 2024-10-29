#
# @lc app=leetcode id=2866 lang=python3
#
# [2866] Beautiful Towers II
#

# @lc code=start
def get_one_side(maxHeights):
    n = len(maxHeights)
    left = [0] * n
    stack = []
    for i in range(n):
        if not stack:
            left[i] = maxHeights[i]
        elif maxHeights[stack[-1]] <= maxHeights[i]:
            left[i] = maxHeights[i] + left[i-1]
        else:
            while stack and maxHeights[stack[-1]] > maxHeights[i]:
                j = stack.pop()            
            if stack:
                left[i] = maxHeights[i] * (i - stack[-1]) + left[stack[-1]]
            else:
                left[i] = maxHeights[i] * (i + 1) 
        stack.append(i)
    return left

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        left = get_one_side(maxHeights) 
        right = get_one_side(maxHeights[::-1])[::-1]
        total = [left[i]+right[i]-maxHeights[i] for i in range(len(maxHeights))]
        return max(total)
# @lc code=end

