#question:https://www.geeksforgeeks.org/problems/number-of-factors1435/1

from math import sqrt
class Solution:
    def countFactors (self, n):
        result=[]
        for i in range(1,int(sqrt(n)+1)):
            if n%i==0:
                result.append(i)
                if n//i!=i:
                    result.append(n//i)
        return len(result)    
        
        
        