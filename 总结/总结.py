# 二分搜索模版

# 1.如果target存在返回其index，如果target不存在返回 - 1

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return - 1


# 2. 万能模版，处理各种复杂题目
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid

    # 我们得到 【left, right] 闭区间
    # 需要根据题目写具体的逻辑 return left, right, left-1, right+1 etc

# 162. Find Peak Element
# 875. Koko Eating Bananas

# 34. Find First and Last Position of Element in Sorted Array
# 74. Search a 2D Matrix
# 35. Search Insert Position
# 704. Binary Search
# 278. First Bad Version
# 167. Two Sum II - Input Array Is Sorted
# 153. Find Minimum in Rotated Sorted Array
# 367. Valid Perfect Square
# 374. Guess Number Higher or Lower
# 744. Find Smallest Letter Greater Than Target


# 滑动窗口模版
from collections import defaultdict


def sliding_window(s):
    left = 0
    res = 0
    window = defaultdict(int)
    for right in range(len(s)):
        rval = s[right]
        window[rval] += 1

        while window[rval] > 1:
            lval = s[left]
            left += 1
            window[lval] -= 1

        res = max(res, right - left + 1)
    return res


# 3. Longest Substring Without Repeating Characters
# 713. Subarray Product Less Than K
# 76. Minimum Window Substring
# 424. Longest Repeating Character Replacement
# 992. Subarrays with K Different Integers
# 1838. Frequency of the Most Frequent Element


# 1695. Maximum Erasure Value

# 堆模版
# python 优先队列 heapq 是 `min heap`. 最小 element 是 heap[0]
# API:
# qp = heapq.heapify([...])
# heapq.heappush(pq, element)
# heapq.heappop(pq)
# heapq.nlargest(n, iterable, key=None)
# heapq.nsmallest(n, iterable, key=None)


# 767. Reorganize String
# 347. Top K Frequent Elements
# 295. Find Median from Data Stream
# 973. K Closest Points to Origin
# 621. Task Scheduler
# 506. Relative Ranks
# 1046. Last Stone Weight
# 703. Kth Largest Element in a Stream
# 1985. Find the Kth Largest Integer in the Array


# 双指针模版

# bisect.bisect_right: find the first index i such that nums[i] > target
# bisect.bisect_left: find the first index i such that nums[i] >= target
# bisect.bisect_left is equivalent to bisect_right if target is not in the nums
# bisect.bisect_left find the first target if target is in the nums

# 1. find index greater than target
# bisect.bisect_right(nums, target)

# 2. find index greater than or equal to target
# bisect.bisect_left(nums, target)

# 3. find index less than target
# bisect.bisect_left(nums, target) - 1

# 4. find index less than or equal to target
# bisect.bisect_right(nums, target) - 1