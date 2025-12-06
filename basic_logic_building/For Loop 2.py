#question:https://www.geeksforgeeks.org/problems/for-loop-2-python/1?page=1&category=python&sortBy=submissions
def stringJumper(s):
    for i in range(0,len(s),2):
        # from 0 to length of str and skip 2
        print(s[i], end="")
        #printing character and separating characters by nothing