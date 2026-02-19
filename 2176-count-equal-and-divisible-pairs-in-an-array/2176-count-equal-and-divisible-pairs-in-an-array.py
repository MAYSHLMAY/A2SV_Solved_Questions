from collections import defaultdict

class Solution:
    def countPairs(self, nums, k):
        count = 0
        freq = defaultdict(list)

        for i, v in enumerate(nums):
            freq[v].append(i)
        
        print(freq)

        for num, f in freq.items():
            bucket = [0] * k 
            n = len(f)
            
            for i in f:
                r = i % k
                for r2 in range(k):
                    if (r * r2) % k == 0: count += bucket[r2]
                bucket[r] += 1  

        return count
