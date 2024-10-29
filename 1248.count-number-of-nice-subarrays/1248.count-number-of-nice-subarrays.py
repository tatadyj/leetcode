#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        count = 0 
        ans = 0
        while right < len(nums):
            rval = nums[right]
            right += 1

            # update window
            if rval % 2 == 1:
                count += 1

            while count == k:
                ans += 1
                lval = nums[left]
                left += 1 

                if lval % 2 == 1:
                    count -= 1

        return ans 


# @lc code=end

