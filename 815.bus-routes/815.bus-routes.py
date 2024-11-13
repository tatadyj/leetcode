#
# @lc app=leetcode id=815 lang=python3
#
# [815] Bus Routes
#

# @lc code=start
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        stop2bus = defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                stop2bus[stop].append(i)

        queue = deque([(source, 0)])
        visited_stop = set([source])
        visited_bus = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_stop, step = queue.popleft()
                for bus in stop2bus[curr_stop]:
                    if bus in visited_bus: continue
                    visited_bus.add(bus)
                    for nxt_stop in routes[bus]:
                        if nxt_stop in visited_stop: continue
                        if nxt_stop == target:
                            return step + 1
                        queue.append((nxt_stop, step+1))
                        visited_stop.add(nxt_stop)

        return -1
# @lc code=end

