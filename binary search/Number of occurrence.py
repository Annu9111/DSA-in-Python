#question :https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
class Solution:
    def countFreq(self, arr, target):
        #method 1
        a={}
        for i in arr:
            if a.get(i):
                a[i]=a[i]+1
            else:
                a[i]=1
        
        return a.get(target,0)
        
        #method2
        
        count=0
        for i in range(len(arr)):
            if arr[i]==target:
                count+=1
        return count      
        
    
        
        
        
        