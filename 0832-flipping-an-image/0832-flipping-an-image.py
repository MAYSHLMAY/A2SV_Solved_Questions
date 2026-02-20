class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
            for row in image:
               row[:] = [1 - x for x in row[::-1]]
            return image