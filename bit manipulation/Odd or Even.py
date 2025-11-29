#question:https://www.geeksforgeeks.org/problems/odd-or-even3618/1
class Solution:
    def isEven (self, n):
        if (n&1)==0:
            return True
        else:
            return False