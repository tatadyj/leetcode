#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start

from collections import defaultdict
   def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        unique_char = set() 
        left, right = 0, 0 
        while right < len(s):
            rval = s[right]
            if rval not in unique_char:
                unique_char.add(rval)
                res = max(res, right - left + 1)

            else:
                while rval in unique_char:
                    lval = s[left]
                    left += 1
                    if lval in unique_char:
                        unique_char.remove(lval)

                unique_char.add(rval)

            right += 1

        return res

def template(s):
    res = 0
    left = 0 
    window = defaultdict(int)

    for right in range(len(s)): # [left, right]
        rval = s[right]
        # 更新窗口内数据
        window[rval] += 1

        # 判断左窗口是否收缩
        while window[rval] > 1:
            lval = s[left]
            left += 1
            # 更新窗口内数据
            window[lval] -= 1
    
        res = max(res, right - left + 1)

    return res 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return template(s)

Solution().lengthOfLongestSubstring("abcabcbb")
# @lc code=end

