from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        count = defaultdict(lambda: -1)

        for i in nums2:
            while stack and i > stack[-1]:
                c = stack.pop()
                count[c] = i
            stack.append(i)

        while stack: count[stack.pop()] = -1

        final = []
        for i in nums1: final.append(count[i])

        return final