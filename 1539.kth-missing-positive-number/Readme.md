很容易想到二分搜值， 但是我们并不能确定mid是不是missing。 
所以我们计算 M = number of element <= mid - 1, T = number of element in the array <= mid - 1，
M - T = number of missing number <= mid - 1，如果 M - T < k - 1, mid 肯定不是kth， 需要 left + 1
如果 M - T > k - 1, mid也肯定不是kth, 需要 right - 1， 如果 M - T == k - 1, mid有可能是也有可能不是，因为mid有可能在array里，即下一个是kth，
所以此时 mid = left。

为什么此算法会converge到kth missing呢？ 因为其实在找最大的一个val，使得[1, val-1]有k-1个missing。
