import sys
from collections import deque

# graph는 graph[0] = [1,2,3] 무 ㅓ 이런식일테니까 
def dfs(start):
    visited[start] = True
    print(start, end = ' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

    # 인접한거 다 방문하고 나서 출력 

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    # 인접한거 큐에 넣어버리고 바로바로 출력 
    

N,M,V = map(int,sys.stdin.readline().split())
visited = [False] * (N+1)
graph = [ [] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(V)
print()
visited = [False] * (N+1)
bfs(V)

# 아 문제 조건에 '정점 번호가 작은 것을 먼저 방문' 이라는 조건이 있었다.