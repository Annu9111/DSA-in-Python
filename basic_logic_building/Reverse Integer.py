# Question: https://leetcode.com/problems/reverse-integer/description/


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
    
        sign= -1 if x<0 else 1
        n=abs(x)
        a=""
        while n>0:
            last_digit=n%10
            a+=str(last_digit)
            n=n//10    
        return sign* int(a) if a else 0

        # if x==0:
        #     return 0

        # n=abs(x)
        # a=[]
        # while n>0:
        #     last_digit=n%10
        #     a.append(str(last_digit))
        #     n=n//10
        # b="".join(a)
        # return int(b)

        if x==0:
            return 0

        sign=-1 if x<0 else 1
        result=0
        n=abs(x)
        while n>0:
            last_digit=n%10
            result=(result*10)+last_digit
            n=n//10
        return sign*result     

        