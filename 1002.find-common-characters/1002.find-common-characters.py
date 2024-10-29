#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        hash = [0] * 26
        for i,c in enumerate(words[0]):
            hash[ord(c) - ord('a')] += 1

        for i in range(1, len(words)):
            hash_other = [0] * 26
            for j in range(len(words[i])):
                hash_other[ord(words[i][j]) - ord('a')] += 1
            for k in range(26):
                hash[k] = min(hash[k], hash_other[k])

        for i in range(26):
            while hash[i] != 0:
                res.append(chr(i + ord('a')))
                hash[i] -= 1
        return res
# @lc code=end

