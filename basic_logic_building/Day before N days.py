#question:https://www.geeksforgeeks.org/problems/days-before-n-days--150030/1?page=1&category=python&sortBy=submissions
class Solution:
    def findAnswer(self, d, n): 
        if n<=6:
           return (abs(n-d))
        else: 
            b=n%7
            return abs(b-d+1)    