class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        final = []

        for num in set(nums2):
            if num in set(nums1):
                final.append(num)
        return final
        
        