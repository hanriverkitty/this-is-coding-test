import sys
INF = sys.maxsize
input  = sys.stdin.readline
n,m,c = map(int,input().split())
visited = [False] *(n+1)
distance = [INF] *(n+1)


graph = [[]for _ in range(n+1)]
for i in range(m):
    q,w,e = map(int,input().split())
    graph[q].append((w,e))

#최단거리인 노드의 index 리턴
def smallest():
    min_value = INF
    index = 0
    for i in range(n+1):
        if distance[i]<min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

#다익스트라 알고리즘
def dijkstra(c):
    distance[c]=0
    visited[c]=True
    
    #일단 연결된 노드들의 거리 저장
    for i in graph[c]:
        distance[i[0]] = i[1]
    
    #현재노드를 제외한 모든 노드 탐색
    for i in range(n-1):
        now = smallest()
        visited[now]=True
        for j in graph[now]:
            cost = distance[now]+j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
dijkstra(c)
cnt=0
dis_sum=0
#방문했던곳들 탐색 총 걸리는 시간은 제일 멀리있는 노드까지 걸리는 시간이다
for i in range(n+1):
    if visited[i]==True:
        dis_sum = max(dis_sum,distance[i])
        cnt+=1

#시작노드의 방문은 count하면 안되므로 -1
print(cnt-1 ,dis_sum)