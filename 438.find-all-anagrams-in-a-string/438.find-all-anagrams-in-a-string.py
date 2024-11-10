#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import defaultdict, Counter
from typing import List 

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = defaultdict(int)
        res = []

        left = 0 
        valid = 0 

        for right in range(len(s)):
            rval = s[right]

            # update window 
            if rval in need:
                window[rval] += 1 
                if window[rval] == need[rval]:
                    valid += 1 

            print(f"window: [{left}, {right})\n")
            while right - left + 1 == len(p):
                if valid == len(need):
                    res.append(left) 

                lval = s[left]
                left += 1 

                if lval in need:
                    if window[lval] == need[lval]:
                        valid -= 1 
                    window[lval] -= 1 
        
        return res 

Solution().findAnagrams("cbaebabacd","abc")     
# @lc code=end

