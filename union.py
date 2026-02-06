class Solution:    
    def findUnion(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        union = list(set(a) | set(b))
        # union.sort() 
        return union