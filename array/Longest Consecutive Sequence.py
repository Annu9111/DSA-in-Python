#question:https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest=float("-inf")
        count=0
        my_set=set(nums)
        for i in my_set:
            if i-1 not in my_set:
                x=i
                count=1
                while x+1 in my_set:
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest
                