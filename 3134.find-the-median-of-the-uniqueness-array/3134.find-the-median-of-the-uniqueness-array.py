#
# @lc app=leetcode id=3134 lang=python3
#
# [3134] Find the Median of the Uniqueness Array
#

# @lc code=start
class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        def count_less_or_equal(val):
            count = 0
            freq = defaultdict(int)
            l = 0 
            for r in range(n):
                rval = nums[r]
                freq[rval] += 1
            
                while len(freq) > val:
                    lval = nums[l]
                    freq[lval] -= 1 
                    if freq[lval] == 0: 
                        freq.pop(lval)
                    l += 1

                count += r-l+1
            return count

        n = len(nums)
        left = 1
        right = n
        N = n*(n+1)/2

        while left < right:
            mid = (left + right) // 2
            count = count_less_or_equal(mid)
            if count >= (N+1)//2:
                right = mid 
            else:
                left = mid + 1
        return left 

        
# @lc code=end

