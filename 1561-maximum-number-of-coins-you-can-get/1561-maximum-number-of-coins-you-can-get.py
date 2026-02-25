class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        final = 0
        right = len(piles) - 1

        for _ in range(len(piles) // 3):
            right -= 1
            final += piles[right]
            right -= 1
        return final