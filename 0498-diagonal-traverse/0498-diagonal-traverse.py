class Solution:
    def findDiagonalOrder(self, mat):
        n, m = len(mat), len(mat[0])
        final = []

        r = c = 0
        dr, dc = -1, 1

        for _ in range(n * m):
            final.append(mat[r][c])

            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
               
                if dc == 1:
                    if c + 1 < m:
                        c += 1
                    else:
                        r += 1
                
                else:
                    if r + 1 < n:
                        r += 1
                    else:
                        c += 1

                dr *= -1
                dc *= -1
            else:
                r, c = nr, nc

        return final