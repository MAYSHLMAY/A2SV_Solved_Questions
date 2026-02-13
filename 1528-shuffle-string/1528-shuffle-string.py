class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        m = [0] * len(s)
        i = 0
        for indice in indices:
            m[indice] = s[i]
            print(s[indice])
            i += 1
        return "".join(m)