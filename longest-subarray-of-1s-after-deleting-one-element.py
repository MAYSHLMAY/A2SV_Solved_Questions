class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0

        final = 0
        m = 0

        for r in range(len(nums)):

            if (nums[r] == 0): m += 1

            while (m > 1):
    
                if nums[l] == 0: m -= 1
                l += 1

            final = max(final, r - l)
        return final
