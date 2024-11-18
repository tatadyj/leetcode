#
# @lc app=leetcode id=1234 lang=python3
#
# [1234] Replace the Substring for Balanced String
#

# @lc code=start
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        is_balanced = True
        freq = Counter(s)
        for k,v in freq.items():
            if v != n/4:
                is_balanced = False
        if is_balanced:
            return 0 

        def is_ok():
            for k in freq:
                if k in window:
                    if freq[k] - window[k] > n/4:
                        return False 
                else:
                    if freq[k] > n/4:
                        return False 
            return True 
            
        res = n - 1
        window = defaultdict(int)
        left = 0 
        for right in range(len(s)):
            rval = s[right]
            window[rval] += 1

            while is_ok():
                res = min(res, right-left+1)
                lval = s[left]
                window[lval] -= 1
                if window[lval] == 0:
                    window.pop(lval)
                left += 1

        return res
            



# @lc code=end

