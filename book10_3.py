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
parent = [0] * (v+1)

edges = []
result = []

for i in range(1,v+1):
    parent[i]=i
    
for i in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for i in edges:
    cost,a,b = i
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result.append(cost)
        
print(sum(result)-max(result))
