#https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1
class Solution:
    def nextLargerElement(self, arr):
        result=[]
        for i in range(len(arr)):
            found=False
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i]:
                    found=True
                    result.append(arr[j])
                    break
            if not found:
                result.append(-1)
        return result        