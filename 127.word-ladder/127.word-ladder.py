#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from typing import List 

from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dict = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:]
                dict[key].append(word)
        
        queue = deque()
        visited = set()

        queue.append(beginWord)
        visited.add(beginWord)
        step = 1 
        while queue:
            size = len(queue)

            for _ in range(size):
                curr = queue.popleft()
                if curr == endWord:
                    return step 

                for i in range(len(curr)):
                    next = curr[:i] + '*' + curr[i+1:]
                    for w in dict[next]:
                        if w not in visited:
                            visited.add(w)
                            queue.append(w)
            step += 1
        return 0

# @lc code=end

