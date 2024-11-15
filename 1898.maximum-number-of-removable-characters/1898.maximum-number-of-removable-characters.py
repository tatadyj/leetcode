#
# @lc app=leetcode id=1898 lang=python3
#
# [1898] Maximum Number of Removable Characters
#

# @lc code=start
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        removable = {v:i for i,v in enumerate(removable)}
        
        def is_ok(k):
            j = 0 
            for i in range(len(s)):
                if j < len(p) and s[i] == p[j]:
                    if i in removable and removable[i] >= k:
                        j += 1
                    if i not in removable:
                        j += 1
            return j == len(p)

        left = 0 
        right = len(removable)
        while left < right:
            mid = (left + right + 1) // 2
            if is_ok(mid):
                left = mid 
            else:
                right = mid - 1
        return left 
# @lc code=end

