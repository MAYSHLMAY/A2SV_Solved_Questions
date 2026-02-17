class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        count1 = defaultdict(str)
        count2 = defaultdict(str)

        if len(s) != len(pattern): 
            return False
        for i in range(len(pattern)):

            a, b = pattern[i], s[i]
            if a in count1 and count1[a] != b:
                return False
            if b in count2 and count2[b] != a:
                return False
            count1[a] = b
            count2[b] = a

        return True
