#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#

# @lc code=start
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_dict = defaultdict(list)
        in_degree = defaultdict(int)
        for word in words:
            for c in word:
                in_degree[c] = 0

        for i in range(len(words)-1):
            s = words[i]
            t = words[i+1]
            if len(s) > len(t) and s[:len(t)] == t:
                return ""
            j = 0
            while j < min(len(s), len(t)):
                if s[j] != t[j]: 
                    adj_dict[s[j]].append(t[j])
                    in_degree[t[j]] += 1
                    break # 碰到第一个不同就可以停止
                j += 1

        queue = deque()
        for c in in_degree:
            if in_degree[c] == 0:
                queue.append(c)

        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for nxt in adj_dict[curr]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)
        if len(res) != len(in_degree):
            return ""
        else:
            return ''.join(res)



# @lc code=end

