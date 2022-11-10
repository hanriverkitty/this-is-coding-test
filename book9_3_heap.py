import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m,c = map(int,input().split())
distance = [INF] *(n+1)


graph = [[]for _ in range(n+1)]
for i in range(m):
    q,w,e = map(int,input().split())
    graph[q].append((w,e))
    
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)
cnt=0
value = 0
for i in distance:
    if i!=INF:
        cnt+=1
        value=max(value,i)

print(cnt-1,value)