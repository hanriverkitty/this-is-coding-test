import sys
n,k = map(int,sys.stdin.readline().split())
arr1 = list(map(int,sys.stdin.readline().rstrip().split()))
arr2 = list(map(int,sys.stdin.readline().rstrip().split()))


arr1.sort()
arr2.sort(reverse=True)

for i in range(int(k)):
    if arr1[i]<arr2[i]:
        arr1[i],arr2[i] = arr2[i],arr1[i]
    
print(sum(arr1))