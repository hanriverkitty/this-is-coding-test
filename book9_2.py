import sys
input = sys.stdin.readline
n , m = map(int,input().split())
INF = int(1e9)
graph = [[INF]*(n+1)for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
for i in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1


x,k = map(int,input().split())

for i in range(1,n+1):
    for j in range(1,n+1):
        for l in range(1,n+1):
            graph[j][l] = min(graph[j][l],graph[j][i]+graph[i][l])
            graph[l][j] = min(graph[l][j],graph[l][i]+graph[i][j])



if graph[1][k] != INF and graph[k][x] != INF :
    print(graph[1][k]+graph[k][x])
else:
    print(-1)