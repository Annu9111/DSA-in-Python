#question:https://leetcode.com/problems/asteroid-collision/description/
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        n=len(asteroids)
        stack=[]
        for i in range(0,n):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:
                while len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                    stack.pop()   
                if len(stack)!=0 and stack[-1]==abs(asteroids[i]):
                    stack.pop()
                elif len(stack)==0 or stack[-1]<0:
                    stack.append(asteroids[i])
        return stack                       
        