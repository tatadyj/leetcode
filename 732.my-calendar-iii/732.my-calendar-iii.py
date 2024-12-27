#
# @lc app=leetcode id=732 lang=python3
#
# [732] My Calendar III
#

# @lc code=start
from sortedcontainers import SortedDict 

class MyCalendarThree:
    '''
    对于前闭后开区间, e.g. [2, 6), 
    如果是模版1：list append [time, +1/-1]，在开区间我们要先处理-1，然后处理1
    这样开区间处的count才是正确的。
    如果是模版2: dict[time] += 1，也是正确

    '''

    def __init__(self):
        self.calendar = SortedDict()

        

    def book(self, startTime: int, endTime: int) -> int:
        self.calendar[startTime] = self.calendar.get(startTime, 0) + 1
        self.calendar[endTime] = self.calendar.get(endTime, 0) - 1
        res = 0 
        sum = 0
        for v in self.calendar.values():
            sum += v 
            res = max(res, sum)
        return res  


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)
# @lc code=end

