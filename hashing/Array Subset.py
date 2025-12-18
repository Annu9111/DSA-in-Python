# https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?page=1&category=Hash,python&difficulty=Basic&sortBy=submissions
#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        my_dict={}
        
        for i in a:
            my_dict[i]=my_dict.get(i,0)+1
        
        for i in b:
            if i in my_dict and my_dict[i]>0:
                my_dict[i]-=1
            else:
                return False
        return True        
            
    
    
    
    
