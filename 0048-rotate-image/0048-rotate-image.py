class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        layers = len(matrix) // 2

        for i in range(layers):

            first = i
            last = len(matrix) - 1 - i

            for j in range(first, last):
                offset = j - first

                top = matrix[first][j]
                matrix[first][j] = matrix[last - offset][first] 
                matrix[last - offset][first] = matrix[last][last - offset]  
                matrix[last][last - offset] = matrix[j][last] 
                matrix[j][last] = top  
