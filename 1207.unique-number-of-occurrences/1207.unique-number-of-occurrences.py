#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = [0] * 2002
        for i in range(len(arr)):
            count[arr[i] + 1000] += 1
        freq = [False] * 1002
        for i in range(200)
# @lc code=end

