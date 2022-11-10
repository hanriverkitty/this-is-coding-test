n,m = map(int,input().split())
won = []
for i in range(n):
    won.append(int(input()))
arr = [10001 for _ in range(m+1)]
arr[0]=0

for i in range(n):
    for j in range(won[i],m+1):
        if(arr[j]!=10001):
            arr[j] = min(arr[j],arr[j-won[i]]+1)
            

if arr[m]==10001:
    print(-1)
else:
    print(arr[m])

    