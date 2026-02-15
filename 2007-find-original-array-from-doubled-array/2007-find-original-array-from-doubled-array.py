class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        print(changed)

        counts = Counter(changed)
        final = []

        for num in changed:
            if counts[num] == 0: continue
            counts[num] -= 1

            double = num * 2
    
            if counts[double] > 0:
                counts[double] -= 1
                final.append(num)
            else:
                return []
        
        return final
                