#
# @lc app=leetcode id=2564 lang=python3
#
# [2564] Substring XOR Queries
#

# @lc code=start
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        map = defaultdict(list)
        for i in range(len(queries)):
            a, b = queries[i]
            map[a^b].append(i)
        
        n = len(s)
        res = [[-1, -1] for _ in range(len(queries))]
        for k in range(1, 32):
            sum = 0
            for i in range(n):
                sum =  sum * 2 + int(s[i])
                if i-k >= 0:
                    sum -= int(s[i-k])*2**k
                if i-k+1 >= 0:
                    if sum in map:
                        for idx in map[sum]:
                            if res[idx][0] == -1:
                                res[idx] = [i-k+1, i]
        return res  
# @lc code=end

