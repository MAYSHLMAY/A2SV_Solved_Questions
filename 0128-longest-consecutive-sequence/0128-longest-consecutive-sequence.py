class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique = set(nums)
        max_count = 0
        for num in unique:
            if num - 1 not in unique:
                length = 0
                while (num + length in unique):
                    length += 1
                max_count = max(max_count, length)
        return max_count

