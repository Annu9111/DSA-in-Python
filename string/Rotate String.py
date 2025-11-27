#question:https://leetcode.com/problems/rotate-string/description/
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        a=list(s)
        b=list(goal)
        for i in range(len(a)):
            e=a.pop()
            a.insert(0,e)
            if a==b:
                return True
        return False        
        