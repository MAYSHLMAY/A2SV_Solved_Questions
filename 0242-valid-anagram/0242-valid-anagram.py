class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counts = Counter(s)
        if len(s) != len(t): return False
        for i in t:
            if i in counts:
                counts[i] -= 1
                if counts[i] == 0: del counts[i]
            else: return False
        return not counts