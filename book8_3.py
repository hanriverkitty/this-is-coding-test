n = int(input())
k = list(map(int,input().split()))
arr = [0 for _ in range(n+1)]
for i in range(1,n+1):
    arr[i] = k[i-1]
arr[1]=k[0]
arr[2]=max(k[0],k[1])
for i in range(3,n+1):
    arr[i] = max(k[i-1]+arr[i-2],arr[i-1])

print(arr[n])