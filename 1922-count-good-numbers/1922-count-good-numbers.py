class Solution:
    def countGoodNumbers(self, n: int) -> int:

        m = 10**9 + 7
        n1 = (n + 1) // 2
        n2 = n // 2


        return (pow(5, n1, m) * pow(4, n2, m)) % (10**9 + 7)



        