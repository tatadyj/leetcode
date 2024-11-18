#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
def at_most_method(self, nums: List[int], goal: int) -> int:
    def at_most(goal):
        if goal < 0:
            return 0 
            
        sum = 0
        left = 0 
        count = 0
        for right in range(len(nums)):
            rval = nums[right]
            sum += rval 

            while left < len(nums) and sum > goal:
                lval = nums[left]
                sum -= lval 
                left += 1
            
            count += right - left + 1
        return count
    #print(at_most(goal), at_most(goal-1))
    return at_most(goal) - at_most(goal-1)

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # prefix_j - prefix_i = goal
        # prefix_i = prefix_j - goal

        prefix = [0] + nums
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] + prefix[i]

        map = defaultdict(int)
        map[0] = 1
        res = 0
        n = len(nums)
        for i in range(n):
            if prefix[i+1] - goal in map:
                res += map[prefix[i+1] - goal]
            map[prefix[i+1]] += 1
        return res            

        
# @lc code=end

