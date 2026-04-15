class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def kmost(k: int):
            l = 0
            seen = defaultdict(int)
            count = 0

            for r in range(len(nums)):

                seen[nums[r]] += 1

                while (len(seen) > k):
                    
                    seen[nums[l]] -= 1
                    if (seen[nums[l]] == 0): del seen[nums[l]]
                    l += 1
                
                count += r - l + 1
            return count
        return kmost(k) - kmost(k - 1)
            
