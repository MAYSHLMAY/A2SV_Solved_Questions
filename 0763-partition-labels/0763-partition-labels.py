class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        

        i = 0
        j = 0

        counter = defaultdict(int)
        for m in range(len(s)): counter[s[m]] = m
        final = []


        for k in range(len(s)):

           print(s[k])
           j = max(j, counter[s[k]])

           if (k == j):
            final.append(j - i + 1)
            i = j + 1
        

        return final