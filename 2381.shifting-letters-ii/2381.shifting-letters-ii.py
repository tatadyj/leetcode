#
# @lc app=leetcode id=2381 lang=python3
#
# [2381] Shifting Letters II
#

# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = defaultdict(int)
        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1
       
        pos = sorted(diff.keys())
        s = list(s)
        sum = 0
        j = 0
        for i in range(len(s)):
            while j < len(pos) and pos[j] <= i:
                sum += diff[pos[j]]
                j += 1
            s[i] = chr( ord('a') + (ord(s[i]) - ord('a') + sum) % 26 )
        return ''.join(s)  
# @lc code=end

