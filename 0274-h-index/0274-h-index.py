class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        max_i = 0


        for i in range(len(citations)):
            if (citations[i] >= i + 1):
                max_i = max(max_i, i + 1)

        return max_i
