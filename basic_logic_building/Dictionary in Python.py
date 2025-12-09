#question:  https://www.geeksforgeeks.org/problems/dictionary-in-python-ii/1?page=1&category=python&sortBy=submissions
def pair_sum(arr, sum):
    # code here
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==sum:
                return True
    return False            
        