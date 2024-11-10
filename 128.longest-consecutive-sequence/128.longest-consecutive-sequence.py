#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Union_Find:
    def __init__(self, nums):
        self.parent = {num:num for num in nums}
        self.size = {num:1 for num in nums}
        self.max_size = 1

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_i, node_j):
        root_i = self.find(node_i)
        root_j = self.find(node_j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                self.parent[root_i] = root_j 
                self.size[root_j] += self.size[root_i]
                self.max_size = max(self.max_size, self.size[root_j])
            else:
                self.parent[root_j] = root_i
                self.size[root_i] += self.size[root_j]
                self.max_size = max(self.max_size, self.size[root_i])


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uf = Union_Find(nums)
        unique = set()
        for num in nums:
            unique.add(num)
            if num - 1 in unique: uf.union(num, num-1)
            if num + 1 in unique: uf.union(num, num+1)
        return uf.max_size
        
        
# @lc code=end

