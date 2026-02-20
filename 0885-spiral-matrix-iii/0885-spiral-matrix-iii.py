class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        final = [[rStart, cStart]]
        r, c = rStart, cStart

        steps = 1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = 0

        while (len(final) < rows * cols):

            for _ in range(2):
                
                dr, dc = dirs[m % 4]
                for _ in range(steps):
                    r += dr
                    c += dc

                    if 0 <= r < rows and 0 <= c < cols:
                        final.append([r, c])
                m += 1
            steps += 1
        return final

        