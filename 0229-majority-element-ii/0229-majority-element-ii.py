class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count1 = 0
        count2 = 0

        candidate1 = None
        candidate2 = None

        for num in nums:

            if (candidate1 is not None and (num == candidate1)):
                candidate1 = num
                count1 += 1
            elif (candidate2 is not None and (num == candidate2)):
                candidate2 = num
                count2 += 1
            elif (count1 == 0):
                candidate1 = num
                count1 = 1
            elif (count2 == 0):
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        

        result = []
        limit = len(nums) // 3
        
        if candidate1 is not None and nums.count(candidate1) > limit:
            result.append(candidate1)
        if candidate2 is not None and nums.count(candidate2) > limit:
            result.append(candidate2)
        return result
            
        