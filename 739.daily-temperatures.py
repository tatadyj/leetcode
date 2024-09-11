#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
import enum

# 单调栈经典题
# 1。 判断从栈尾到栈都是单调递增还是单调递减。
# 假设每个元素都没有符合条件的在右侧比它更大的元素，构建的单调栈从栈尾到栈头是单调递减的
# 比如 【73， 69， 63， 43
# 2. 对于任何一个元素， 如果找到符合条件的在右侧比它更大的元素， 此元素必定从栈内pop out
# 因为所根据上面一条，留在栈内的元素都是没有找到符合条件的
# 3. 单调栈记录的是元素的index， 而不是元素本身。 最主要的原因是由返回值决定
# 我们需要更新返回值list中对应的值， 所以要知道比如69在返回值list中的index
# 否则的话需要定义一个dict来解决对应问题 
# 4. 返回值初始化，用找不到符合条件的默认值，此题0

def short_version(temperatures):
    answer = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    return answer 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 初始化返回值， 在找不到符合条件情况下，默认是0
        answer = [0] * len(temperatures)
        stack = [0]

        for i in range(1, len(temperatures)):
            # 当下元素小于等于栈头元素，当下元素不符合条件
            # 当下元素的index 直接入栈
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                # 当下元素大于栈头元素， 符合条件
                # pop 栈头元素， 记录index差值
                # while循环， 直到下一步如果把当下元素push入栈， 单调栈仍然保持单调递减
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    j = stack.pop()
                    answer[j] = i - j 
                stack.append(i)

        return answer
# @lc code=end

