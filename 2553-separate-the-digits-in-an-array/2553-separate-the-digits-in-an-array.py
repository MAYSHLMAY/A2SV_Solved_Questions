class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        final = []
        
        for num in nums:

            power = 10 ** int(math.log10(num))
            while power > 0:
                digit = num // power
                final.append(digit)
                num %= power

                power //= 10
        return final