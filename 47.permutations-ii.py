#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
def bt(ans, permutation, N, nums, is_used):
    if len(permutation) == N:
        ans.append(permutation.copy())
        return 
    
    tmp = None
    for i,num in enumerate(nums):
        if is_used[i] == False and num != tmp: 
            permutation.append(num)
            is_used[i] = True
            bt(ans, permutation, N, nums, is_used)
            tmp = permutation.pop()
            is_used[i] = False


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans, permutation = [], []
        nums.sort()
        is_used = [False] * len(nums)
        bt(ans, permutation, len(nums), nums, is_used)
        return ans
# @lc code=end

