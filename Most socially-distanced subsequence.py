from collections import defaultdict

class Solution:
    def solution(self):
        
        t = int(input())
        
        for _ in range(t):
            
            s = int(input())
            c = list(map(int, input().split()))
            
            final = [c[0]]
            for i in range(1, s-1):
                if ((c[i] - c[i - 1]) * (c[i + 1] - c[i]) < 0):
                    final.append(c[i])
                
            
            final.append(c[len(c) - 1])
            
            
            print(len(final))
            print(*final)
        
        
        
if __name__ == '__main__':
    sol = Solution()
    sol.solution()
