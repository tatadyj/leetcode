#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dict = {n:i for i, n in enumerate(sorted(score, reverse=True))}
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        return [medals[dict[n]] if dict[n] < 3 else str(dict[n]+1) for n in score]
# @lc code=end

