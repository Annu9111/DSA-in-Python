#question:https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1
class Solution:
    def findUnion(self, a, b):
        c=a+b
        dic={}
        for i in c:
            if dic.get(i):
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        a=[]
        for i in dic:
            a.append(i)
        return sorted(a)   
        
        
        
        
        # return sorted(list(set(a)| set(b)))