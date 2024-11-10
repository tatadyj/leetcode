from collections import defaultdict 
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 0
        left = 0 
        window = defaultdict(int)
        
        for right in range(len(s)):
            rval = s[right]
            # update window
            window[rval] += 1
            
            while len(window) > 2:
                lval = s[left]
                left += 1 
                
                # update window
                window[lval] -= 1
                if window[lval] == 0:
                    window.pop(lval)
                    
            res = max(res, right - left + 1)
            
        return res 
