找第k小的质分数，二分搜索。 arr是排过序的 arr[i] / arr[j] < 1

问题简化： 

给定一个值， 如何O(n)时间count多少个质分数 <= 这个值。 可以用滑窗解决。 
由于给定的值是小数，`left = mid, right = mid` 
