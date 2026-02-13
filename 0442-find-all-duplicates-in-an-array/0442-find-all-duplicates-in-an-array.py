class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        final = []
        for i in nums:
            i = abs(i)

            if (nums[i - 1] < 0): final.append(i)
            else: nums[i - 1] = - nums[i - 1]

        return final