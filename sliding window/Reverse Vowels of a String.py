#question:
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=set("aeiouAEIOU")
        nums=list(s)
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l] not in vowels:
                l+=1
            elif nums[r] not in vowels:
                r-=1
            else:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        return "".join(nums)                 
      

        