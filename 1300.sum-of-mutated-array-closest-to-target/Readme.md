随便猜一个值，立马知道sum是大于还是小于target。 这里我们用二分搜索找最接近target并且大于target的那个值x。 然后与x-1比较一下， 看那个数更接近target。 

我们可以用O(logn)的方法去求sum。 首先我们意识到arr的顺序无所谓，先对arr排序，然后第二次用二分搜索找idx，使其对应的元素值大于mid。
然后用prefix sum O(1)的时间计算新的sum。 
