# https://leetcode.com/problems/perfect-number/description/?envType=problem-list-v2&envId=math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        result=[]
        n=num
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                result.append(i)
                if n//i!=i:
                    result.append(n//i)
        ans=0            

        for i in result:
            if i!=num:
                ans+=i 
        return ans==num                   

        