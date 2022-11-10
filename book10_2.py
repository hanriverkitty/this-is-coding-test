def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,c,d):
    c = find_parent(parent,c)
    d = find_parent(parent,d)
    if c>d:
        parent[c]=d
    else:
        parent[d]=c

v, e = map(int,input().split())
parent=[0]*(v+1)

for i in range (1,v+1):
    parent[i]=i

result=[]

for i in range(e):
    num,a,b = map(int,input().split())
    if num == 0:
        union_parent(parent,a,b)
    elif num == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            result.append("YES")
        else:
            result.append("NO")

for i in result:
    print(i)