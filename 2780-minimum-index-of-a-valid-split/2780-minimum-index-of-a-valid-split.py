class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for x in nums: counts[x] += 1
        
        valid = None
        total = 0
        for x in counts:
            if counts[x] * 2 > len(nums):
                valid = x
                total = counts[x]
                break
        
        if valid is None: return -1
        left_valid = 0
       
        for i in range(len(nums) - 1):
            if nums[i] == valid:
                left_valid += 1
            
            right_valid = total - left_valid
            
            left_len = i + 1
            right_len = len(nums) - left_len
            
            if left_valid * 2 > left_len and right_valid * 2 > right_len:
                return i
                
        return -1