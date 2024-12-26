#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#

# @lc code=start
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n = len(arr)
        arr.sort()
        res = 0
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                if arr[i] + arr[left] + arr[right] < target:
                    left += 1
                elif arr[i] + arr[left] + arr[right] > target:
                    right -= 1
                else:
                    if arr[left] != arr[right]: 
                        count_left, count_right = 1, 1
                        while left < right and arr[left] == arr[left+1]: 
                            left += 1
                            count_left += 1
                        while left < right and arr[right] == arr[right-1]: 
                            right -= 1
                            count_right += 1
                        res += count_left * count_right
                    else: 
                        l = right - left + 1
                        # Cn_2 = n*(n-1)/2
                        cnt = l * (l - 1) // 2
                        res += cnt
                        break 

                    left += 1
                    right -= 1
        return res % (10**9 + 7)
# @lc code=end

