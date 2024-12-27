#
# @lc app=leetcode id=1589 lang=python3
#
# [1589] Maximum Sum Obtained of Any Permutation
#

# @lc code=start
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)

        request_dict = defaultdict(int)
        for start, end in requests:
            request_dict[start] += 1
            request_dict[end + 1] -= 1

        n = len(nums)
        freq = [0] * (n+1)
        for pos in sorted(request_dict):
            freq[pos] = request_dict[pos]
        
        for i in range(1, n):
            freq[i] = freq[i-1] + freq[i]

        freq.sort(reverse=True)
        res = 0
        for i in range(n):
            res += freq[i] * nums[i]
        return res % (10**9 +7)

# @lc code=end

