#
# @lc app=leetcode id=1300 lang=python3
#
# [1300] Sum of Mutated Array Closest to Target
#

# @lc code=start
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # def get_sum(val):
        #     return sum([min(v, val) for v in arr])

        # if sum(arr) <= target:
        #     return max(arr)

        arr.sort()
        prefix_sum = [0] + arr
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i-1] + prefix_sum[i]
        
        if prefix_sum[-1] <= target: 
            return arr[-1]

        n = len(arr)
        def get_sum(val):
            idx = bisect.bisect_right(arr, val) # first element > val 
            return prefix_sum[idx] + val * (n - idx)


        left = 0
        right = max(arr)

        while left < right:
            mid = (left + right) // 2
            val = get_sum(mid)
            if val >= target:
                right = mid 
            else:
                left = mid + 1
                
        v1 = abs(get_sum(left) - target)
        v2 = abs(get_sum(left - 1) - target)
        if v1 < v2:
            return left
        else:
            return left - 1  
# @lc code=end

