#question:https://www.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1?page=1&category=Strings,python&difficulty=Easy&sortBy=submissions
#User function Template for python3
class Solution:


    def removeDuplicates(self, s):
        seen=set()
        result=[]
        for i in s:
            if i not in seen:
                seen.add(i)
            result.append(i)
        return "".join(result)	            
	        
	    
	    