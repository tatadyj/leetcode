#
# @lc app=leetcode id=2963 lang=python3
#
# [2963] Count the Number of Good Partitions
#

# @lc code=start
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        # 根据题意，任何相同的数字必须在同一个subarray
        n = len(nums)
        right = defaultdict(int)
        left = defaultdict(int)
        for i in range(n):
            right[nums[i]] = i

        for i in range(n-1, -1, -1):
            left[nums[i]] = i 

        diff = defaultdict(int)
        for num in sorted(left):
            diff[left[num]] += 1
            diff[right[num]] -= 1
        
        sum = 0 
        count = 0
        for k in sorted(diff):
            sum += diff[k]
            if sum == 0:
                count += 1

        return 2**(count-1) %(10**9+7)

# @lc code=end

