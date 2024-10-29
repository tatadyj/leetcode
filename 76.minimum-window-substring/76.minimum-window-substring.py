#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import defaultdict, Counter
def template(s, t):
        need = Counter(t)
        window = defaultdict(int)

        left = 0 
        valid = 0
        minWindow = float('inf')
        for right in range(len(s)): # [left, right]
            # rval 是将移入窗口的字符
            rval = s[right]
            # 窗口内数据更新
            if rval in need:
                window[rval] += 1    
                if window[rval] == need[rval]:
                    valid += 1 
            # 判断左窗口是否收缩
            while valid == len(need):
                if right - left + 1 < minWindow: # 最小窗口
                    start = left
                    minWindow = right -left + 1 

                lval = s[left]
                left += 1
                # 窗口内数据更新
                if lval in need:
                    if window[lval] == need[lval]:
                        valid -= 1 
                    window[lval] -= 1

        if minWindow == float('inf'):
            return ""
        else:
            return s[start:start+minWindow]

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return template(s, t)

print(Solution().minWindow("ADOBECODEBANC", "ABC"))
# @lc code=end

