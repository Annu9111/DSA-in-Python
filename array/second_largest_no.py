#question :https://www.naukri.com/code360/problems/ninja-and-the-second-order-elements_6581960

def getSecondOrderElements(n: int,  a):
    
    largest=float("-inf")
    s_largest=float("-inf")
    smallest=float("inf")
    s_smallest=float("inf")
    
    for i in a:
        largest=max(largest,i)
        smallest=min(smallest,i)
    
    for i in range(n):
        if a[i]!=largest:
            s_largest=max(s_largest,a[i])
        if a[i]!=smallest:
            s_smallest=min(s_smallest,a[i])
    
    return [s_largest,s_smallest]                