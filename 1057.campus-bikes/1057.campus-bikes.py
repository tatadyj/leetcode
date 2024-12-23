#
# @lc app=leetcode id=1057 lang=python3
#
# [1057] Campus Bikes
#

# @lc code=start
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def find_distance(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        worker_bike_list = []
        pq = []
        for w, worker in enumerate(workers):
            curr_pairs = []
            for b, bike in enumerate(bikes):
                dist = find_distance(worker, bike)
                curr_pairs.append((dist, w, b))
            curr_pairs.sort(reverse=True)
            heapq.heappush(pq, curr_pairs.pop())
            worker_bike_list.append(curr_pairs)

        bike_status = [False] * len(bikes)
        worker_status = [-1] * len(workers)

        while pq:
            dist, w, b = heapq.heappop(pq)
            if not bike_status[b]:
                bike_status[b] = True 
                worker_status[w] = b 
            else:
                nxt_closest_bike = worker_bike_list[w].pop()
                heapq.heappush(pq, nxt_closest_bike)

        return worker_status    
# @lc code=end

