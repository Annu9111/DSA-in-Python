#question:https://www.geeksforgeeks.org/problems/better-string/1
#User function Template for python3
class Solution:

    def solve(self,index,subset,nums,result):
        if index>=len(nums):
            result.add("".join(subset))
            return
        subset.append(nums[index])
        self.solve(index+1,subset,nums,result)
        subset.pop()
        self.solve(index+1,subset,nums,result)
            
    
    
    def betterString(self, s1, s2):
        result1=set()
        result2=set()
        
        self.solve(0,[],list(s1),result1)
    
        
        self.solve(0,[],list(s2),result2)
        
        
        # if len(result2)>len(result2):
        #     return s2
        # else:
        #     return s1
        return s2 if len(result2)>len(result1) else s1
        