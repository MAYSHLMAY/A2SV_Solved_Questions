class Solution:
    def minSteps(self, s: str, t: str) -> int:

        counts = Counter(s)
        y = 0
        for i in t:
            if i in counts:
                counts[i] -= 1
                if (counts[i] == 0): del counts[i]
            else:
                y += 1
        return y
