class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        r = len(matrix)
        c = len(matrix[0])

        transpose = [[] for _ in range(c)]


        for i in range(c):
            for j in range(r):
                transpose[i].append(matrix[j][i])


        return transpose