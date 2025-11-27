#question:https://www.naukri.com/code360/problems/implement-upper-bound_8165383?leftPanelTabValue=PROBLEM
def upperBound(arr: [int], x: int, n: int) -> int:

    ans=n
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>x:
            ans=mid
            high=mid -1
        else:
            low=mid+1
    return ans 