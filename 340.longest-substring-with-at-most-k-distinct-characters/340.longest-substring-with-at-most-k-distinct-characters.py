from collections import defaultdict 

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        left = 0 
        window = defaultdict(int)
        
        for right in range(len(s)):
            rval = s[right]
            # update window
            window[rval] += 1
            
            while len(window) > k:
                lval = s[left]
                left += 1 
                
                # update window
                window[lval] -= 1
                if window[lval] == 0:
                    window.pop(lval)
                    
            res = max(res, right - left + 1)
            
        return res 
