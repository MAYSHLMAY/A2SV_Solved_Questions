class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        count = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement not in count:
                count[num] = i
            else: 
                return [count[complement], i]
     
            