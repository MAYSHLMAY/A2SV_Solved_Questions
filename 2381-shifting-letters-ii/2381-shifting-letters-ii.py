from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        m = list(s)
        n = len(s)
        c = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                c[start] += 1
                c[end + 1] -= 1
            else:
                c[start] -= 1
                c[end + 1] += 1

        for i in range(1, n): c[i] += c[i - 1]

        for i in range(n):
            m[i] = chr((ord(m[i]) - ord('a') + c[i]) % 26 + ord('a'))

        return ''.join(m)