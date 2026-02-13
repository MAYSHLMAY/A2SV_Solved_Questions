class Solution:

    def square_digit(self, n: int) -> int:
        final_sum = 0
        while n > 0:
            digit = n % 10
            n = n // 10
            final_sum += digit * digit
        return final_sum


    def isHappy(self, n: int) -> bool:

        fast = n
        slow = n

        while (True):
            slow = self.square_digit(slow)
            fast = self.square_digit(self.square_digit(fast))

            if (fast == 1): return True
            if (fast == slow): return False
    
        