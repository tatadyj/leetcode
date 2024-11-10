#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
def bt(ans, path, nums, used):
    if len(path) == len(nums):
        ans.append(path[:])
        return 

    for i in range(len(nums)):
        # [1, 1, 2] 碰到第二个1时， skip它， 此时第一个1是还没有被选过
        if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
            continue 
        if not used[i]:
            used[i] = True 
            path.append(nums[i])
            bt(ans, path, nums, used)
            path.pop()
            used[i] = False


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

