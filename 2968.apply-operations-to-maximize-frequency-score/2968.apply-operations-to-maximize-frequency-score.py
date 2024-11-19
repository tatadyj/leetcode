#
# @lc app=leetcode id=2968 lang=python3
#
# [2968] Apply Operations to Maximize Frequency Score
#

# @lc code=start
def bs():
    nums.sort()
    nums.insert(0, 0)
    prefix_sum = [0] * len(nums)
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i-1] + nums[i]


    def is_ok(size):
        for i in range(1, len(nums)-size+1):
            j = i + size -1
            m = (i + j) // 2
            sum = nums[m] * (m-i) - (prefix_sum[m-1] - prefix_sum[i-1]) \
                    + (prefix_sum[j] - prefix_sum[m]) - nums[m] * (j-m)  
            if sum <= k:
                return True 
        return False 

    left = 1
    right = len(nums) - 1 # insert 0
    while left < right:
        mid = (left + right + 1) // 2
        if is_ok(mid):
            left = mid 
        else:
            right = mid - 1
    return left 

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.insert(0, 0)
        prefix_sum = [0] * len(nums)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        def get_sum(i, j):
            m = (i + j) // 2
            sum = nums[m] * (m-i) - (prefix_sum[m-1] - prefix_sum[i-1]) \
                    + (prefix_sum[j] - prefix_sum[m]) - nums[m] * (j-m)  
            return sum 
        
        res = 0
        i = 1
        for j in range(1, len(nums)):
            while get_sum(i, j) > k:
                i += 1
            res = max(res, j-i+1)
        return res
         
# @lc code=end

