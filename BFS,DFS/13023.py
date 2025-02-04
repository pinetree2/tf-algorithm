#DFS 같다. 시작점으로부터 이어진 거리가 4 이상이 되면 return 1하면될것같다.

import sys 

def dfs(start,visited,cnt):
    global answer
    
    if cnt == 4:
        answer = 1 
        return 
    
    visited[start] = True
    for next in graph[start]:
        if not visited[next]:
            dfs(next,visited,cnt+1)

    visited[start] = False # 다시 방문할 수 있도록 초기화
 
    
N,M = map(int,sys.stdin.readline().split())

found = False
graph = [ [] for _ in range(N)]


for _ in range(M):
    a,b = map(int,sys.stdin.readline().split()) 
    graph[a].append(b)
    graph[b].append(a)


# 모든노드가 다 시작점이 될 수 있음 
for i in range(N):
    answer = 0
    visited = [False for _ in range(N)]
    dfs(i,visited,0)
    if answer == 1:
        print(answer)
        break
else:
    print(0)

