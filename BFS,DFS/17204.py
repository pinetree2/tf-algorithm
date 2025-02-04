# 보성이가 M이라고 말해야만 함
# 영기가 불러야 하는 가장 작은 수 M은 ?

# K 다음 노드가 M이다.

import sys
from collections import deque

def bfs(start):
    global count
    queue = deque([start])
    #visited[start] = True

    for _ in range(N):
        v = queue.popleft()
        count +=1
        
        if graph[v] == K: #보성이 
            return count
        
        next_person = graph[v]
        #if not visited[next_person]:  # 방문하지 않은 사람만 큐에 넣음
            #visited[next_person] = True
        queue.append(next_person)
                              
    return -1
    


N,K = map(int,sys.stdin.readline().split())
graph = []
count =0 
visited = [False] * N  # 방문 여부를 기록

for _ in range(N):
    graph.append(int(sys.stdin.readline()))

print(bfs(0))

'''

문제를 정확히 해결하려면 다음을 고려해야 합니다:

시작점(0번 사람)에서 출발해, 보성이가 부르는 순서까지의 경로를 탐색해야 합니다.
보성이가 부르는 순간까지의 경로 길이를 세어야 하므로, BFS를 수정해 이 경로 길이를 반환해야 합니다.

'''