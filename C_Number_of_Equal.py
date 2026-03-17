class Solution:
    def solution(self):
        n, m = map(int, input().split())
        
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        
        i = j = 0
        
        final = 0
        
        while i < n and j < m:
            
            if (a[i] < b[j]): i += 1
            elif (a[i] > b[j]): j += 1
            else:
                
                current = a[i]
                count_a = 0
                count_b = 0
                
                
                while (i < n and a[i] == current):
                    count_a += 1
                    i += 1
                while(j < m and b[j] == current):
                    count_b += 1
                    j += 1
                    
                    
                final += count_a * count_b
            
        print(final)

if __name__ == '__main__':
    sol = Solution()
    sol.solution()
