#question:https://leetcode.com/problems/palindrome-number/description/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n=x
        result=0
        while n>0:
            id=n%10
            result=(result*10)+id
            n=n//10
        return x==result 
