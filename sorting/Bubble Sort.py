#question: https://www.geeksforgeeks.org/problems/bubble-sort/1
class Solution:
    def bubbleSort(self,arr):
        n=len(arr)
        for i in range(n-2,-1,-1):
            for j in range(0,i+1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr            