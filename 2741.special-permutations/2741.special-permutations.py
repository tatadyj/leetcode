#
# @lc app=leetcode id=2741 lang=python3
#
# [2741] Special Permutations
#

# @lc code=start
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        # bitmask state help for memo
        # used = [False] * n 
        ans = 0
        memo = defaultdict(dict)
        def dfs(curr_pos, prev_val, state):
            nonlocal ans
            if curr_pos == n:
                return 1

            if state in memo[prev_val]:
                return memo[prev_val][state]

            count = 0
            for i in range(n):
                if not prev_val: # == 0
                    count += dfs(curr_pos+1, nums[i], state+(1<<i))
                else:
                    if (state >> i) & 1: continue
                    if nums[i] % prev_val != 0 and prev_val % nums[i] != 0: continue
                    count += dfs(curr_pos+1, nums[i], state+(1<<i))
            
           
            memo[prev_val][state] = count
            return count
        return dfs(0, 0, 0) % (10**9 + 7)        
# @lc code=end

