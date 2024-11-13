找kth小的pair distance， 二分搜索。 

问题简化：

给定一个pair distance， 如何在O(n)的时间内，统计多少对pair的pair distance小于等于给定pair distance。 
首先我们关心的是pair， nums顺序无关紧要，所以我们先排序，然后用滑窗。
