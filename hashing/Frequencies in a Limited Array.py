#question:https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0

class Solution:
    def frequencyCount(self, arr):
        d={}
        result=[]
        for i in arr:
            d[i]=d.get(i,0)+1
            
        for i in range(1,len(arr)+1): 
            a=d.get(i,0)
            result.append(a)
            
        return result    
            

