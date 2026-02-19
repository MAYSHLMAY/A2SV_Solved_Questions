class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        n = len(img)
        m = len(img[0])
        directions = [-1, 0, 1]

        final = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):

                total = 0
                c = 0

                for dx in directions:
                    for dy in directions:
                        dni = i + dx
                        dnj = j + dy

                        if 0 <= dni < n and 0 <= dnj < m:
                            total += img[dni][dnj]
                            c += 1
                final[i][j] = total // c
        return final

