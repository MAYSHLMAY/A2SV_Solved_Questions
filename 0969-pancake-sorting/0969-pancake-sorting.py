class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        final = []
        n = len(arr)
        for c in range(n, 1, -1):
            m = 0
            for i in range(1, c):
                if arr[i] > arr[m]: m = i

            if m == c - 1: continue
            if m != 0:
                arr[:m+1] = arr[:m+1][::-1]
                final.append(m + 1)

            arr[:c] = arr[:c][::-1]
            final.append(c)

        return final