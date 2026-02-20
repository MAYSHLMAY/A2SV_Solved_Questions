class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        maxNumber = max(nums)
        count = [0] * (maxNumber + 1)
        final = []

        for num in nums: count[num] += 1
        print(count)
        for i in range(1, maxNumber + 1): count[i] += count[i-1]

        for num in nums:
            if num == 0: final.append(0)
            else: final.append(count[num-1])  
        return final