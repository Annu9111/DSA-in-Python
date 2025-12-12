#question:https://www.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1?page=1&category=Strings,python&difficulty=Easy&sortBy=submissions
class Solution:
    def isRotated(self,s1,s2):
        #code here
        if len(s1)!=len(s2):
            return False
        anticlockwise= s1[2:]+ s1[:2]
        clockwise= s1[-2:] +s1[:-2]
        
        return s2==anticlockwise or s2==clockwise