#queation:https://leetcode.com/problems/happy-number/description/?envType=problem-list-v2&envId=hash-table
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        my_set=set()
        while n not in my_set:
            my_set.add(n)
            n=self.sumofsquare(n)

            if n==1:
                return True
        return False

    def sumofsquare(self,n):
        output=0
        while n>0:
            digit=n%10
            digit=digit**2
            output+=digit
            n=n//10
        return output                    
        