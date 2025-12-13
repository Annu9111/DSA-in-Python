#question:https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1?page=1&category=Strings,python&sortBy=submissions
class Solution:
    def areRotations(self, s1, s2):
        if len(s1)!=len(s2):
            return False
        
        a=list(s1)
        b=list(s2)

        # for i in range(len(b)):
        #     if a==b:
        #         return True
        #     else:
        #         # e=a.pop()
        #         # a.insert(0,e)
        #         a=a[-1:] +a[:-1]
        # return False        
        
        return s2 in (s1+s1)        
        