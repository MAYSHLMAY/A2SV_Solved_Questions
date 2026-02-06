class Solution:
    def checkEqual(self, a, b) -> bool:
  
        unique = {}
        if len(a) != len(b): return False
        
        for i in a:
            unique[i] = unique.get(i, 0) + 1;
        
        for j in b:
            if j in unique:
                unique[j] -= 1;
                if (unique.get(j, 0) == 0): del unique[j]

                
        
        if not unique:
            return True
        else: return False