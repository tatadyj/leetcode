#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#

# @lc code=start
from sortedcontainers import SortedList 

class MyCalendarTwo:

    def __init__(self):
        self.calendar = SortedList()
        

    def book(self, startTime: int, endTime: int) -> bool:
        self.calendar.add([startTime, 1])
        self.calendar.add([endTime, -1])

        sum = 0 
        for t, v in self.calendar:
            sum += v 
            if sum == 3:
                self.calendar.remove([startTime, 1])
                self.calendar.remove([endTime, -1])
                return False 
        return True
            

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
# @lc code=end

