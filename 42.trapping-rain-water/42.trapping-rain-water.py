#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start

def monostack(height):
    # 单调栈
    '''
    单调栈是按照 行 的方向来计算雨水
    从栈底到栈顶的顺序：从大到小
    通过三个元素来接水：栈顶，栈顶的下一个元素，以及即将入栈的元素
    雨水高度是 min(凹槽左边高度, 凹槽右边高度) - 凹槽底部高度
    雨水的宽度是 凹槽右边的下标 - 凹槽左边的下标 - 1 (因为只求中间宽度)
    '''    
    # stack储存index，用于计算对应的柱子高度
    stack = [0]
    res = 0 

    for i in range(1, len(height)):
        # case 1
        if height[i] < height[stack[-1]]:
            stack.append(i)

        # case 2 
        # 当当前柱子高度和栈顶相同时，左边（栈顶）是不能存放雨水的
        elif height[i] == height[stack[-1]]:
            stack.pop()
            stack.append(i)

        # case 3 
        else:
            while stack and height[i] > height[stack[-1]]:
                mid = height[stack[-1]]
                stack.pop()
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    # 两侧较矮的一方作为高度， 然后减去凹槽底部高度
                    h = min(right, left) - mid 
                    # 凹槽右侧index - 凹槽左侧index - 1， 只有中间能装水
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
    return res 

class Solution:
    def trap(self, height: List[int]) -> int:
        #return monostack(height)
        ans = 0 
        leftMax, rightMax = 0, 0
        left, right = 0, len(height)-1
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                ans += leftMax - height[left]
                left += 1 
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans 
# @lc code=end

