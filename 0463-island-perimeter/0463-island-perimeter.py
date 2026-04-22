class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        final = 0
        d = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    p = 4

                    for a, b in d:
                        ni = i + a
                        nj = j + b

                        if 0 <= ni < n and 0 <= nj < m:
                            if grid[ni][nj] == 1: p -= 1

                    final += p

        return final