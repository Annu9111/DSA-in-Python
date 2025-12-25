# https://leetcode.com/problems/build-an-array-with-stack-operations/description/?envType=problem-list-v2&envId=dsa-linear-shoal-stack
class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack=[]
        i=0
        for j in range(1,n+1):
            stack.append("Push")
            if target[i]==j:
                i+=1
                if i==len(target):
                    break
            else:
                stack.append("Pop")
        return stack                       

    
        