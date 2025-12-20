# https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1?page=1&category=Sorting,python&sortBy=submissions
class Solution:
    def sort012(self, arr):
        # result=[]
        # for i in range(0,len(arr)):
        #     min=i
        #     for j in range(i+1,len(arr)):
        #         if arr[j]<arr[min]:
        #             min=j
        #     arr[i],arr[min]=arr[min],arr[i]
        # return arr  
        
        
        c0,c1,c2=0,0,0
        for i in arr:
            if i==0:
                c0+=1
            elif i==1:
                c1+=1
            else:
                c2+=1
        index=0
        for _ in range(c0):
            arr[index]=0
            index+=1
        
        for _ in range(c1):
            arr[index]=1
            index+=1
            
        for _ in range(c2):
            arr[index]=2
            index+=1
        return arr   
        
        
        
        
        
        
        