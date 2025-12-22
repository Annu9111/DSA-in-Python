# https://www.geeksforgeeks.org/problems/find-the-odd-occurence4820/1?page=1&category=Hash,python&difficulty=Basic&sortBy=submissions
class Solution:
    def getOddOccurrence(self, arr):
        my_dict={}
        for i in arr:
            my_dict[i]=my_dict.get(i,0)+1
        for key,values in my_dict.items():
            if values%2!=0:
                return key
                