# https://leetcode.com/problems/self-dividing-numbers/description/?envType=problem-list-v2&envId=math
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result=[]
        for i in range(left,right+1):
            check=True
            temp=i
            while temp>0:
                digit=temp%10
                if digit==0 or i%digit!=0:
                    check=False   
                    break
                temp=temp//10
            if check:
                result.append(i)
        return result                              

        