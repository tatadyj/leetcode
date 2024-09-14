#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List 

def short():
    heights.append(0)
    heights.insert(0,0)
    stack = []
    res = 0
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            idx = stack.pop()
            h = heights[idx]
            right_smaller = i
            if stack:
                left_smaller = stack[-1]
                res = max(res, h * (right_smaller - left_smaller - 1))
        
        stack.append(i)

    return res 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic Stack
        '''
        找每个柱子左侧和右侧的next samaller元素
        维护一个单调递增栈：栈底到栈顶，从小到大
        每次遇到一个比栈顶小的元素时候，就找到了右边的next smaller 
        每次pop栈顶元素时，就是记录以当前元素作为高，左边延伸到left next smaller 右边延伸到right next smaller 
        的矩形面积
        需要在左右两边补上0，来解决左边或者右边没有next smaller，也就是默认next smaller就是这两个0
        '''
        heights.append(0)

        # 输入数组首尾各补上一个0（与42.接雨水不同的是，本题原首尾的两个柱子可以作为核心柱进行最大面积尝试
        heights.insert(0,0)
        stack= [0]
        res = 0 

        for i in range(1, len(heights)):
            # case 1 
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            # case 2
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            # case 3
            else:
                # pop 栈里所有较高的柱子
                while stack and heights[i] < heights[stack[-1]]:
                    # 栈顶就是中间柱子，形成的矩形高度由它决定
                    mid = stack[-1]
                    stack.pop()
                    if stack:
                        left = stack[-1]
                        right = i 
                        w = right - left - 1
                        h = heights[mid] # 矩形高度
                        res = max(res, w * h)
                stack.append(i)

        return res  
        
print(Solution().largestRectangleArea([1,2,3]))
# @lc code=end

