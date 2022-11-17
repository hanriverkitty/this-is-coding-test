n,m=map(int,input().split())
arr = list(map(int,input().split()))
# cnt=0
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             continue
#         if arr[i]==arr[j]:
#             continue
#         else:
#             cnt+=1
# print(cnt//2)
result=0
array=[0]*11
for x in arr:
    array[x]+=1

for i in range(1,m+1):
    n-=array[i]
    result += array[i] * n