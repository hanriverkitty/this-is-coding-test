import sys
N = int(input())
arr = list(map(int,sys.stdin.readline().rstrip().split()))
M=int(input())
c_arr = list(map(int,sys.stdin.readline().rstrip().split()))
arr.sort()

def binary_serch(arr,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    if(arr[mid]==target):
        return True
    elif arr[mid]>target:
        return binary_serch(arr,target,start,mid-1)
    else:
        return binary_serch(arr,target,mid+1,end)

for i in c_arr:
    if (binary_serch(arr,i,0,N-1))==True:
        print("yes", end=" ")
    else:
        print("no", end=" ")
    