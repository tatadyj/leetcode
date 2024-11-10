#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.valToIndex = {}

        

    def insert(self, val: int) -> bool:
        if val in self.valToIndex:
            return False

        self.valToIndex[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valToIndex:
            return False 
        # 取出val的索引
        index, lastItem = self.valToIndex[val], self.nums[-1]
        # 更改最后一个元素的索引
        self.valToIndex[lastItem] = index
        
        # 交换val和最后一个元素
        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        # 删除val及其索引
        self.nums.pop()
        self.valToIndex.pop(val)
        return True 

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

