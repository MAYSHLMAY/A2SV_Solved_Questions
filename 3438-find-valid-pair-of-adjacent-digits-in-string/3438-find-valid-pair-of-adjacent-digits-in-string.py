class Solution:
    def findValidPair(self, s: str) -> str:

        counts = Counter(s)
        print(counts)
        
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                if (counts[s[i]] == int(s[i]) and counts[s[i + 1]] == int(s[i + 1])): return f"{s[i]}{s[i+1]}"
        
        return ""
            
            

        