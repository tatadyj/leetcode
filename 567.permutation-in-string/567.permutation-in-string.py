#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = defaultdict(int)

        left = 0 
        valid = 0

        for right in range(len(s2)): #[left, right]
            rval = s2[right]
            # update window 
            if rval in need:
                window[rval] += 1 
                if window[rval] == need[rval]:
                    valid += 1
            print(f"window: [{left}, {right})\n")
            # determine whether to reduce window
            while right - left + 1 == len(s1):
                if valid == len(need):
                    return True 

                lval = s2[left]
                left += 1 
                # update window
                if lval in need:
                    if window[lval] == need[lval]:
                        valid -= 1
                    window[lval] -= 1

        return False 


Solution().checkInclusion("ab","eidbaooo")

# @lc code=end

