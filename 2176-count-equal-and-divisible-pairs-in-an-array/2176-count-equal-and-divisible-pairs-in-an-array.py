from collections import defaultdict

class Solution:
    def countPairs(self, nums, k):
        count = 0
        freq = defaultdict(list)
        
        for i, v in enumerate(nums):
            freq[v].append(i)
        
        print(freq)

        for num, f in freq.items():
            n = len(f)
            if n >= 2:
                for i in range(n):
                    for j in range(i + 1, n):
                        if (f[i] * f[j]) % k == 0:
                            count += 1

        return count
