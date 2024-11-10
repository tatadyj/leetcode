#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        if k == 0:
            count = 0 
            for v in freq:
                if freq[v] > 1:
                    count += 1
            return count

        arr = sorted(freq.keys())
        res = 0
        left = 0 
        for right in range(len(arr)):
            while arr[right] - arr[left] > k:
                lval = arr[left]
                left += 1

            if arr[right] - arr[left] == k:
                res += 1
        return res 
        
# @lc code=end

