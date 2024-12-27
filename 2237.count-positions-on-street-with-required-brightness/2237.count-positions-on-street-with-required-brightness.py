class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        diff = defaultdict(int)
        for pos, rng in lights:
            diff[max(0, pos-rng)] += 1
            diff[min(n-1, pos+rng)+1] -= 1
        
        pos = sorted(diff.keys())
        count = 0
        sum = 0
        j = 0
        for i in range(n):
            while j < len(pos) and pos[j] <= i:
                sum += diff[pos[j]]
                j += 1
            if sum >= requirement[i]:
                count += 1
        return count