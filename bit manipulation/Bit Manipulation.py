#question:https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1
#User function Template for python3

class Solution:
    def bitManipulation(self, num, i):
        get_bit= (num>>(i-1)) & 1
        set_bit= num | (1<<(i-1))
        clear_bit= num & ~(1<<(i-1))
        return [get_bit,set_bit,clear_bit]