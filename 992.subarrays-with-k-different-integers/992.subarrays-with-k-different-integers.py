#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(nums, k):
            res = 0 
            left = 0 
            window = defaultdict(int)
            for right in range(len(nums)):
                rval = nums[right]
                window[rval] += 1 

                while len(window) > k:
                    lval = nums[left]
                    window[lval] -= 1
                    if window[lval] == 0:
                        window.pop(lval)
                    left += 1 
                
                res += right - left + 1
            return res 

        return at_most_k(nums, k) - at_most_k(nums, k-1)
        
# @lc code=end

