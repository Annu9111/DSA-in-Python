#question:https://www.geeksforgeeks.org/problems/roman-number-to-integer3201/1?page=1&category=Strings,python&difficulty=Easy&sortBy=submissions
class Solution:
    def romanToDecimal(self, s): 
        count=0
        my_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            if i+1<len(s) and my_dict[s[i]] < my_dict[s[i+1]]:
                count-=my_dict[s[i]]
            else:
                count+=my_dict[s[i]]
        return count 