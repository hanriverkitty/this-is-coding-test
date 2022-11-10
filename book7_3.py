import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

def binary_search(arr,start,end,m):
    if start>end:
        return end
    mid = (start+end)//2
    sum = 0
    for i in arr:
        if(i>=mid):
            sum+=i-mid
        if sum>m:
            break
    
    if sum>=m:
        return binary_search(arr,mid+1,end,m)
    else:
        return binary_search(arr,start,mid-1,m)
        
    
    
    
print(binary_search(arr,1,max(arr),m))
