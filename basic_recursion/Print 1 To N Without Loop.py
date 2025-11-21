#question:https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1
#code
class Solution:    
    def printNos(self,n):
        if n==0:
            return 
        self.printNos(n-1)
        print(n,end=" ")