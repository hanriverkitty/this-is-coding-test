from collections import deque

n = int(input())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
time = [0] * (n+1)

for i in range(1,n+1):
    l = list(map(int,input().split()))
    time[i] = l[0]
    for j in l[1:-1]:
        graph[j].append(i)
        indegree[i] +=1   

def topology_sort():
    result=time[:]
    q = deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i],result[now]+time[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    
    for i in result[1:]:
        print(i)
   

topology_sort()