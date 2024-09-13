#
# @lc app=leetcode id=2104 lang=python3
#
# [2104] Sum of Subarray Ranges
#

# @lc code=start
def get_sum_min(arr):
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
    
    return sum_of_min
            
def get_sum_max(arr):
    stack = []
    sum_of_max = 0
    n = len(arr)
    next_larger = [n] * n
    prev_larger = [-1] * n

    # next larger
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            j = stack.pop()
            next_larger[j] = i
        stack.append(i)

    stack.clear() 
    # prev larger
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            j = stack.pop()
            prev_larger[j] = i 
        stack.append(i) 

    for i in range(n):
        sum_of_max += arr[i] * (i - prev_larger[i]) * (next_larger[i] - i)
    
    return sum_of_max
            
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        return get_sum_max(nums) - get_sum_min(nums)
# @lc code=end

