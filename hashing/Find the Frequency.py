#question :https://www.geeksforgeeks.org/problems/find-the-frequency/1

"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        dic={}
        n=len(arr)
        for i in range(n):
            dic[arr[i]]=dic.get(arr[i],0)+1
        return dic.get(x,0)   