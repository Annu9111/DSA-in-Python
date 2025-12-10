#question:https://leetcode.com/problems/check-if-n-and-its-double-exist/description/?envType=problem-list-v2&envId=sorting
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]==arr[j]*2 or arr[i]*2==arr[j]:
                    return True
        return False