class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        final = []
        seen1 = set(nums1)
        seen2 = set(nums2)


        for num in seen1:
            if num in seen2:
                final.append(num)
        return final
        
        