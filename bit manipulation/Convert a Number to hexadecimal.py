#question:https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/?envType=problem-list-v2&envId=string
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        my_dict={10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
        result=""
        if num==0:
            return "0"

        num= num & 0xffffffff  
            

        while num>0:
            a=num%16
            if a<10:
                result+=str(a)
            else:
                result+=my_dict[a]
            num=num//16

        return result[::-1]            