import sys

# 인접한 모든 노드는 감염됨 -> DFS

def dfs(graph,v,visited):
    global count # global count는 함수 내에서 전역 변수를 참조하겠다는 의미입니다. 이는 새로운 변수를 선언하는 것이 아니라, 이미 선언된 전역 변수를 사용하겠다는 것을 나타냅니다.
    count +=1
    visited[v] = True
    #print(v, end = ' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
        

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [ [] for _ in range(N+1)]
visited = [False] * (N+1)
count =0

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort() #1번 컴퓨터부터 시작이니까 

dfs(graph,1,visited) 
print(count-1) # 1번은 이미 감염되었는데 한번 더 세서 그런건가