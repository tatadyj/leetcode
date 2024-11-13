找kth小subarray，用二分搜索
首先一想到subarray sum，就立马想到用prefix sum。 如果给定一个sum，如何用O(n)的时间统计有多少个subarray和小于或等于给定的sum。 
本题的特点是所有的元素都是正的， prefix sum也就是递增的， 可以用滑动窗口来找符合条件的subarray。
