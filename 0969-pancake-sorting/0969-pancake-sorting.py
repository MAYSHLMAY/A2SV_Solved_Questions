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
                self.reverse(arr, 0, m)
                final.append(m + 1)

            self.reverse(arr, 0, c - 1)
            final.append(c)

        return final

    def reverse(self, arr: List[int], left: int, right: int):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1