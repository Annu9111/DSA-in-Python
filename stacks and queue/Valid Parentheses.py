#question:https://leetcode.com/problems/valid-parentheses/description/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """   


        stack=[]
        for i in s:
            if i=="("or i=="{" or i=="[":
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                ch=stack.pop()
                if (i==")" and ch=="(") or (i=="}" and ch=="{") or (i=="]" and ch=="[") :
                    continue
                else:
                    return False
        return  len(stack)==0
                            