#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        target = stones[-1]
        stones = set(stones)
        memo = set()
        def dfs(pos, jump):
            if (pos, jump) in memo:
                return False

            if pos == target:
                return True 

            for x in [-1, 0, 1]:
                next_jump = jump + x
                next_pos = pos + next_jump
                if next_jump > 0 and next_pos in stones:
                    if dfs(next_pos, next_jump):
                        return True 
                    else:
                        memo.add((next_pos, next_jump))
            memo.add((pos, jump))
            return False

        return dfs(0, 0)

        
# @lc code=end

