#question:https://www.geeksforgeeks.org/problems/if-loop-python/1?page=1&category=python&sortBy=submissions
def friends_in_trouble(j_angry, s_angry):
    if  j_angry==True and s_angry==True:
        return True
    elif  j_angry==True and s_angry==False:
        return False
    elif  j_angry==False and s_angry==True:
        return False
    else:
        return True
    
    