# https://www.geeksforgeeks.org/problems/count-the-characters1821/1?page=1&category=Hash,python&difficulty=Basic&sortBy=submissions
#User function Template for python3

class Solution:
    def getCount (self,S, N):
        # your code here
        my_dict={}
        my_dict[S[0]]=1
        for i in range(1,len(S)):
            if S[i]!=S[i-1]:
                my_dict[S[i]]=my_dict.get(S[i],0)+1
        
        count=0
        for i in my_dict.values():
            if i==N:
                count+=1
        return count        