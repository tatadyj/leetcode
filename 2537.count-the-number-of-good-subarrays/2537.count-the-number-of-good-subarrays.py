#
# @lc app=leetcode id=2537 lang=python3
#
# [2537] Count the Number of Good Subarrays
#

# @lc code=start
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = defaultdict(int)
        left = 0
        count = 0 
        total = 0
        for right in range(n):
            rval = nums[right]
            if freq[rval] > 0:
                total += freq[rval]
            freq[rval] += 1
            
            while total >= k:
                count += n - right
                lval = nums[left]
                if freq[lval] > 0:
                    total -= freq[lval] - 1
                freq[lval] -= 1
                left += 1
        return count
        
# @lc code=end

