#
# @lc app=leetcode id=1311 lang=python3
#
# [1311] Get Watched Videos by Your Friends
#

# @lc code=start
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        freq = defaultdict(int)
        n = len(watchedVideos)
        queue = deque()
        queue.append((id, 0))
        visited = [False] * n
        visited[id] = True 

        while queue:
            size = len(queue)
            for _ in range(size):
                curr, l = queue.popleft()
                for nxt in friends[curr]:
                    if visited[nxt]: continue 
                    if level == l + 1:
                        for video in watchedVideos[nxt]:
                            freq[video] += 1
                    queue.append((nxt, l+1))
                    visited[nxt] = True 

        res = [(c,v) for v,c in freq.items()]
        res.sort()
        return [v for c,v in res]
        
    
# @lc code=end

