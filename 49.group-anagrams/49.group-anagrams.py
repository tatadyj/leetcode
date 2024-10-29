#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            array = [0] * 26 
            for c in str:
                array[ord(c) - ord('a')] += 1
            res[tuple(array)].append(str)
        return res.values()
        
# @lc code=end

