#question:https://www.geeksforgeeks.org/problems/jumping-through-while-python/1?page=1&category=python&difficulty=Easy&sortBy=submissions
def printIncreasingPower(x):
    #code here
    n=1
    while(n<=x):
        if n**2>x:
            return 
        print (n**2 , end = " ")
        n+=1
        
        