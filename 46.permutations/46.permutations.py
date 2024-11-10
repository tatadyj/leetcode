#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
def bt(ans, permutation, N, nums):
    if len(permutation) == N:
        ans.append(permutation[:])
        return
    
    for num in nums:
        if num not in permutation:
            permutation.append(num)
            bt(ans, permutation, N, nums)
            permutation.pop()
    return

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, permuatation = [], []
        bt(ans, permuatation, len(nums), nums)
        return ans
        
# @lc code=end

