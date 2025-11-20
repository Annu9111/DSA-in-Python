#question :https://www.geeksforgeeks.org/problems/prime-number2314/1

class Solution:
    def isPrime(self, n):
        result=[]
        check=False
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                result.append(i)
                if n//i!=i:
                    result.append(n//i)
                    
        if len(result)==2:
            if n and 1 in result:
                check=True
            
        return check    
        