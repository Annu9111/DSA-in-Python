#question:https://leetcode.com/problems/valid-palindrome-ii/description/?envType=problem-list-v2&envId=string
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        l,r=0,n-1
        while l<r:
            if s[l]!=s[r]:
                skipl,skipr=s[l+1:r+1],s[l:r]
                return (skipl==skipl[::-1]) or (skipr==skipr[::-1])
            r-=1
            l+=1
        return True        

                       

        