#
# @lc app=leetcode id=2014 lang=python3
#
# [2014] Longest Subsequence Repeated k Times
#

# @lc code=start
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)

        t = ''
        for v in freq:
            if freq[v] >= k:
                t += v 
        
        def is_ok(cur):
            if not cur: return True 

            j = 0
            round = 0
            for i in range(len(s)):
                if s[i] != cur[j]: continue 
                j += 1

                if len(cur) == j:
                    j = 0
                    round += 1
                    if round == k:
                        return True 
            return False 

        def dfs(cur):
            nonlocal res 

            if not is_ok(cur):
                return 

            if len(cur) == len(res) and cur > res:
                res = cur 

            if len(cur) > len(res):
                res = cur

            if len(cur) == 7:
                return 

            for ch in t:
                nxt = cur + ch 
                dfs(nxt)

        res = ''
        cur = ''
        dfs(cur)
        return res     
# @lc code=end

