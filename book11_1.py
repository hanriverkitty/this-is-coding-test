# n = int(input())
# arr = list(map(int,input().split()))
# cnt=0

# while arr!=[]:
#     a = min(arr)
#     arr.remove(a)
#     for i in range(a-1):
#         arr.remove(min(arr))
#     if arr==[]:
#         break
#     cnt+=1

# print(cnt)
n = int(input())
arr =list(map(int,input().split()))
arr.sort()

result = 0
count = 0
for i in arr:
    count+=1
    if count >= i:
        result+=1
        count=0
print(result)