class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        m = x
        if m < 0:
            return False

        f = 0
        while x > 0:
            rem = x % 10
            f = 10 * f + rem
            x //= 10

        return f == m
