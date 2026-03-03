class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s = list(s)
        b = defaultdict(int)
        i = 0
        for char in order:
            b[char] = i
            i += 1
        
        s.sort(key=lambda x: b[x])
      
        return "".join(s)