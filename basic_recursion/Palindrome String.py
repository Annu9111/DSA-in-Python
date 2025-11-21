#question :https://www.geeksforgeeks.org/problems/palindrome-string0817/1
#code
class Solution:
    def isPalindrome(self, s):
        # b=s[::-1]
        # return b==s
        
        right=len(s)-1
        for left in range(0,len(s)):
            if s[left]==s[right]:
                left+=1
                right-=1
                if left>=right:
                    return True
            else:
                return False