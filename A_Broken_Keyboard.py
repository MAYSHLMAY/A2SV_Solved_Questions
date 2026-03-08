class Solution:
    def solution(self):
        for _ in range(int(input())):
            
            s = input()
            length = 0
            l, r = 0, 0
            c = []
           
            for _ in range(len(s)):
                
                while (r < len(s) and s[l] == s[r]): r += 1
                length = r - l
                
                if (length % 2 == 1 and l < len(s)): c.append(s[l])
                
                l = r
           
            print("".join(sorted(c)))

if __name__ == '__main__':
    sol = Solution()
    sol.solution()