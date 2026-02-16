from collections import defaultdict
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = defaultdict(int)

        left_max = 0
        left_f = None
        right_max = 0
        right_f = None

        for x in nums:
            right[x] += 1
        
        for key, val in right.items():
            if val > right_max:
                right_max = val
                right_f = key

        n = len(nums)
        for i in range(n - 1): 
            val = nums[i]
            
            left[val] += 1
            if left[val] > left_max:
                left_max = left[val]
                left_f = val

            right[val] -= 1
 
            if val == right_f:
                right_max -= 1

            left_len = i + 1
            right_len = n - left_len
            
            if left_max * 2 > left_len and right_max * 2 > right_len:
                if left_f == right_f:
                    return i

        return -1
