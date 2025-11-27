#question:https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401
def getFloorAndCeil(a, n, x):
    ceil=-1
    floor=-1
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==x:
            return [a[mid],a[mid]]
        elif a[mid]>x:
            ceil=a[mid]
            high=mid-1
        else:
            floor=a[mid]
            low=mid+1    
    return [floor,ceil]     
       
