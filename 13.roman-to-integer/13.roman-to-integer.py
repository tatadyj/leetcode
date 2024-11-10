#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        nums = [dict[w] for w in s]
        ans = 0
        
        i = 0
        while i < len(nums)-1:
            if nums[i] >= nums[i+1]:
                ans += nums[i]
            else:
                ans -= nums[i]
            i += 1
        ans += nums[i]
        return ans

print(Solution().romanToInt("LVIII"))
# @lc code=end

