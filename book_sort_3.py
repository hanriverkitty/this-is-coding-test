import sys
N = int(sys.stdin.readline().strip())
dic={}
for i in range(N):
    a,b = sys.stdin.readline().rstrip().split()
    dic[a]=int(b)
    
print(dic)
s_dic=sorted(dic.items(), key =lambda x : x[1] )
for i in s_dic:
    print(i[0],end=" ")