本题就是考察如何用python二分搜索api，找所要求的idx。 
核心思想对于每一个house， 找到左右两边的那两个heater 位置，看哪个heater离house更近。
选更近的那个计算radius。 遍历所有house找到最大的radius。 需要特殊处理头尾两端情况，此时house只有一个heater。 
