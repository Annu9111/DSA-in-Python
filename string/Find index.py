#question:https://www.geeksforgeeks.org/problems/find-index-1614919939--145853/1?page=1&category=python&sortBy=submissions
#User function Template for python3

arr = tuple(map(int, input().split()))
x = int(input())

########### Write your code below ###############
for i in range(0,len(arr)):
    if arr[i]==x:
        print(i)

########### Write your code above ###############