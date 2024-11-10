#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        sum_of_min = 0
        n = len(arr)
        next_smaller = [n] * n
        prev_smaller = [-1] * n
        # next smaller
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                j = stack.pop()
                next_smaller[j] = i
            stack.append(i)

        stack.clear() 

        # prev smaller
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                j = stack.pop()
                prev_smaller[j] = i 
            stack.append(i) 

        for i in range(n):
            sum_of_min += arr[i] * (i - prev_smaller[i]) * (next_smaller[i] - i)
        
        return sum_of_min % (10**9 + 7)
             
# @lc code=end

