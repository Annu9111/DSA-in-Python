#question:https://www.geeksforgeeks.org/problems/check-the-status/1?page=1&category=python&sortBy=submissions
class Solution:
    def checkStatus(self, a, b, flag):
        if ((a<0 and b>0) or (a>0 and b<0)) and flag==False:
            return True
        if (a<0 and b<0) and flag==True:
            return True
        else:
            return False
        