class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique = set(nums)
        max_count = 0
        for num in unique:
            if num - 1 in unique:
                continue
            curry = num
            current_count = 0
            while (curry in unique):
                current_count += 1
                curry += 1
            max_count = max(max_count, current_count)
        return max_count

