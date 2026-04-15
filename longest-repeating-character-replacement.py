class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        c = defaultdict(int)
        final = 0
        l = 0
        r = 0
        _max = 0


        for r in range(len(s)):

            c[s[r]] += 1
            _max = max(_max, c[s[r]])
         
            while ((r - l + 1) - _max > k):
                c[s[l]] -= 1
                l += 1
            
            final = max(final, r - l + 1)
        return final
