#question :https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set=set()
        for i in nums:
            my_set.add(i)

        my_set=sorted(my_set)
        k=len(my_set)

        j=0
        for i in my_set:
            nums[j] = i
            j+=1

        return k       
        