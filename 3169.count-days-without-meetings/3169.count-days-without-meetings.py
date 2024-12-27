#
# @lc app=leetcode id=3169 lang=python3
#
# [3169] Count Days Without Meetings
#

# @lc code=start
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        差分数组：找哪些天没有被覆盖
        [start, end] inclusive
        """
        diff = defaultdict(int)

        for start, end in meetings:
            diff[start] += 1
            diff[end+1] -= 1 

        diff[days+1] += 1

        
        sum = 0 
        total = 0
        start, end = 1, None
        for pos in sorted(diff):
            if sum == 0 and sum + diff[pos] > 0:
                end = pos
                total += end - start 
            elif sum > 0 and sum + diff[pos] == 0:
                start = pos
            sum += diff[pos]
        return total
  
# @lc code=end

