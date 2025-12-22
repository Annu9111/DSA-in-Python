# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/?envType=problem-list-v2&envId=math
class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def is_prime(n):
            if n<=1:
                return False
            for i in range(2,n):
                if n%i==0:
                    return False
            return True


        ans=0
        for i in range(left,right+1):
            set_bits=bin(i).count("1")
            if is_prime(set_bits):
                ans+=1
        return ans        

                 
        