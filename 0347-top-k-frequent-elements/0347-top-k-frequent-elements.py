class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)
        print(buckets)

        r = []
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]: r.extend(buckets[i])
            if len(r) >= k: return r[:k]