#question:https://leetcode.com/problems/add-digits/description/?envType=problem-list-v2&envId=math
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def addition(n):
            sum=0
            while n>0:
                last_digit=n%10
                sum+=last_digit
                n=n//10
            return sum    

        while num>9:
            num=addition(num)

        return num    
               
        