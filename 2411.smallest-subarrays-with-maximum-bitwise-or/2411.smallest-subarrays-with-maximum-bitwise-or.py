#
# @lc app=leetcode id=2411 lang=python3
#
# [2411] Smallest Subarrays With Maximum Bitwise OR
#

# @lc code=start
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        count = [0] * 32
        n = len(nums)

        def ok_remove(v):
            for k in range(32):
                if count[k] == 1 and (v >> k)&1:
                    return False 
            return True 

        ans = [0] * n
        j = n - 1
        for i in range(n-1, -1, -1):
            for k in range(32):
                count[k] += (nums[i] >> k) & 1
            
            while j > i and ok_remove(nums[j]):
                for k in range(32):
                    count[k] -= (nums[j] >> k) & 1        
                j -= 1
            ans[i] = j - i + 1
        return ans

# @lc code=end

