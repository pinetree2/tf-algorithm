# 최소의 칸 -> bfs
# 시작 정점 -> (1,1)
# 도착 정점 -> (N,M)
# 이동할 수 없는 칸 -> 0
# 이동할 수 있는 칸 -> 1

import sys
from collections import deque


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y)) # 인덱스를 넣는 셈이다.
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == False and graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
                    visited[nx][ny] = True


N,M = map(int,sys.stdin.readline().split())
# M개 만큼 N번 입력받아야 한다.
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)] # strip() : 문자열 앞뒤 공백제거
visited = [[False] * M for _ in range(N)]
bfs(0,0)
print(graph[N-1][M-1]) # 그래프의 마지막 값이 최소값이다.

# 아 vscode 코파일럿때문에... 코드를 작성하는데에 내 생각이 덜 들어가는듯 