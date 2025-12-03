#question:https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        # maxi=0
        # for i in range(0,len(cardPoints)):
        #     my_dict={}
        #     for j in range(i,len(cardPoints)):
        #         my_dict[cardPoints[j]]=my_dict.get(cardPoints[i],0)+1
        #         if len(cardPoints)>k:
        #             break
        #         maxi=max(maxi,sum(my_dict.values()))
        # return maxi 


        n=len(cardPoints)
        if n==k:
            return sum(cardPoints)
        left_sum,right_sum=0,0
        for i in range(0,k):
            left_sum+=cardPoints[i]
        maxi=left_sum
        right_index=n-1
        for i in range(k-1,-1,-1):
            left_sum-=cardPoints[i]
            right_sum+=cardPoints[right_index]
            maxi=max(maxi,left_sum+right_sum)
            right_index-=1
        return maxi                       

        