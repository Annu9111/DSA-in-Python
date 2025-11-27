#Question :https://leetcode.com/problems/remove-outermost-parentheses/description/
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        count=0
        for i in s:
            if i=="(":
                count+=1
                if count>1:
                    result+=i
            else:
                count-=1
                if count>0:
                    result+=i
        return result                    
        







































        