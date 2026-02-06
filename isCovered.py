class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """

        unique = set()
        for start, end in ranges:
            for i in range(start, end + 1):
                unique.add(i)
        
        while (left <= right):
            if (left not in unique):
                return False
            left += 1
        return True
