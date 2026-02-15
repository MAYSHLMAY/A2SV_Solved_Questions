class Solution:
    def frequencySort(self, s: str) -> str:
        
        counts = Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]
        
        for i in counts: buckets[counts[i]].append(i)

        res = []
        for j in range(len(buckets) - 1, 0, -1):
                for k in buckets[j]:
                    res.append(k * j)
        return "".join(res)