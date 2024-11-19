#### 解法1：固定左边界，探索右边界(开区间)
```python
        ret = 0
        count = 0
        freq = defaultdict(int)
        j = 0
        for i in range(len(s)):
            while j < len(s) and count + (freq[s[j]] + 1 == 1) <= k:
                freq[s[j]] += 1
                if freq[s[j]] == 1:
                    count += 1
                j += 1

            ret = max(ret, j-i)
            
            freq[s[i]] -= 1
            if freq[s[i]] == 0:
                count -= 1
        return ret 
```        

#### 解法2：固定右边界，探索左边界(闭区间)
```python
        ret = 0
        count = 0
        freq = defaultdict(int)
        i = 0
        for j in range(len(s)):
            freq[s[j]] += 1
            if freq[s[j]] == 1:
              count += 1
            
            while count > k:
                freq[s[i]] -= 1
                if freq[s[i]] == 0:
                    freq.pop(s[i])
                    count -= 1
                i += 1
            ret = max(ret, j-i+1)
        return ret      
```
