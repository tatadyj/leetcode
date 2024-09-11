#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        need = Counter(words)
        window = defaultdict(int)
        valid = 0 

        k = len(words[0])
        n = len(words)

        left, right = 0, k 
        while right < len(s):
            rword = s[right-k:right] # [0, k)
            right += k 

            # update window
            if rword in need:
                window[rword] += 1
                if window[rword] == need[rword]:
                    valid += 1

            while right - left == n*k:
                if valid == len(words)
                    res.append(left)

                lword = s[left:left+k] # [0, k)
                left += k 

                # update window 
                if lword in need:
                    if window[lword] == need[lword]:
                        valid -= 1 
                    window[lword] -= 1 






        return res 
# @lc code=end

