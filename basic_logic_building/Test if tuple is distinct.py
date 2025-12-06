#question:https://www.geeksforgeeks.org/problems/test-if-tuple-is-distinct/1?page=1&category=python&sortBy=submissions
#User function Template for python3
arr = tuple(map(int, input().split()))

########### Write your code below ###############
# Print "True" if all elements of tuple are different, otherwise print "False"

########### Write your code above ###############
result=[]
for i in range(len(arr)):
    if arr[i] not in result:
        result.append(arr[i])
    else:
        print(False)
        break
if len(result)==len(arr):
    print(True)
    
    
    
    