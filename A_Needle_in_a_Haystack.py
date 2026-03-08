from collections import Counter

class Solution:
    def solution(self):
        for _ in range(int(input())):
           s = input()
           t = input()
           
           count_s = Counter(s)
           count_t = Counter(t)           
           flag = True
                      
           
           for c in count_s:
               if count_s[c] > count_t.get(c, 0):
                   flag = False
                   break
           if not flag:
                print("Impossible")
                continue
               
           left_over_dict = count_t - count_s
           left_over = []
           
           for c in sorted(left_over_dict):
               left_over.extend([c] * left_over_dict[c])
           
           final = []
           needle = list(s)
           i, j = 0, 0
           
           while (i < len(left_over) and j < len(needle)):
               if left_over[i] < needle[j]:
                   final.append(left_over[i])
                   i += 1
               else:
                   final.append(needle[j])
                   j += 1
                   
           final.extend(left_over[i:])
           final.extend(needle[j:])
            
           
           print("".join(final))
           
               
                                  

if __name__ == '__main__':
    sol = Solution()
    sol.solution()