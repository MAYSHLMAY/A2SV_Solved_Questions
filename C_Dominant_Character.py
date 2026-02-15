class Solution:

    def solution(self):
        t = input()
        
        if not t: return
        t = int(t)


        for _ in range(t):

            n = int(input())
            string = input()
            found = False

            for i in range(2, 8):
                for j in range(n - i + 1):
                    sub = string[j: j + i]

                    a = sub.count('a')
                    b = sub.count('b')
                    c = sub.count('c')

                    if a > b and a > c:
                        print(i)
                        found = True
                        break
                if found:
                    break
            if not found: print(-1)



            
if __name__ == "__main__":
    sol = Solution()
    sol.solution()

            