class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        final = []
        even_sum = 0
        for i in nums:
            if i % 2 == 0: even_sum += i

        for val, index in queries:
            
            if (nums[index] % 2 == 0): 
                even_sum -= nums[index]
        
            nums[index] += val

            if (nums[index] % 2 == 0):
                even_sum += nums[index]
            final.append(even_sum)
          
        return final
        

        