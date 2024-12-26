#
# @lc app=leetcode id=2098 lang=python3
#
# [2098] Subsequence of Size K With the Largest Even Sum
#

# @lc code=start
class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        odd, even = [], []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        even.sort(reverse=True)
        odd.sort(reverse=True)

        prefix_even = [0] + even
        for i in range(1, len(prefix_even)):
            prefix_even[i] = prefix_even[i-1] + prefix_even[i]

        prefix_odd = [0] + odd
        for i in range(1, len(prefix_odd)):
            prefix_odd[i] = prefix_odd[i-1] + prefix_odd[i]


        ret = -1
        j = len(even)
        for i in range(min(len(odd), k)+1): # odd 最少取0个最多取k个或者len(odd)个
            while i + j > k:
                j -= 1
            if j < 0:
                break
            if i + j == k and (prefix_odd[i] + prefix_even[j]) % 2 == 0:
                ret = max(ret, prefix_odd[i] + prefix_even[j])         
        return ret  
# @lc code=end

