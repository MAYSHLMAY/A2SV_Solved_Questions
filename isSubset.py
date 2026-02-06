class Solution:

    def isSubset(self, a, b):
        
        unique = {}
        for i in a:
            unique[i] = unique.get(i, 0) + 1;
            
        for j in b:
            if (j in unique):
                unique[j] = unique.get(j, 0) - 1;
                if (unique[j] == 0): del unique[j];
            else:
                return False;
        
        return True