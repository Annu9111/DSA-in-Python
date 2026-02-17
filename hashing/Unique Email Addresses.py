# question:https://leetcode.com/problems/unique-email-addresses/description/?envType=problem-list-v2&envId=hash-table
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_email=set()
        for i in emails:
            local,domain=i.split("@")
            local=local.split("+")[0]
            local=local.replace(".","")
            unique_email.add(local+"@"+domain)
        return len(unique_email)    
         
        