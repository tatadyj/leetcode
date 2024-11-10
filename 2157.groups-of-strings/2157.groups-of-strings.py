#
# @lc app=leetcode id=2157 lang=python3
#
# [2157] Groups of Strings
#

# @lc code=start
class Union_Find:
    def __init__(self, n):
        self.n = n 
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return x 
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.parent[y_root] = x_root

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        def word2state(word):
            state = 0
            for i in range(len(word)):
                ch = ord(word[i]) - ord('a')
                state = state | (1 << ch)
            return state

        n = len(words)
        uf = Union_Find(n)
        states = []
        for word in words:
            states.append(word2state(word))

        state2idx = defaultdict(int)
        for i,state in enumerate(states):
            if state not in state2idx: # words中相同的单词union在一起 eg ab，ba
                state2idx[state] = i 
            else:
                uf.union(i, state2idx[state]) # union by index

        for i in range(n):
            for j in range(26):
                if (states[i] >> j) & 1 == 1:
                    new_state = states[i] - (1 << j)
                    if new_state not in state2idx:
                        state2idx[new_state] = i
                    else:
                        uf.union(i, state2idx[new_state])

        group = defaultdict(int)
        for i in range(n):
            group[uf.find(i)] += 1

        return [len(group), max(group.values())]




        
        
        
# @lc code=end

