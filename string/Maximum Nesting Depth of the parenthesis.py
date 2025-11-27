#Questionhttps://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        if "(" not in s:
            return 0
        maxi=float("-inf")
        count=0
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
                maxi=max(maxi,count)
            if s[i]==")":
                count-=1
                maxi=max(maxi,count)
        return maxi     
