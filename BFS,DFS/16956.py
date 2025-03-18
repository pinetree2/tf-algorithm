'''
import sys 
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 울타리를 놓는 함수 
def bfs(x,y):
    # . 는 빈칸, S는 양, W는 늑대, D는 울타리 
    # 울타리 설치해도 갈수있으면 0 을 출력, 갈수없으면 1 (늑대 존재 x의 경우에도)
    # 울타리 몇개 설치해도 상관없는거임? 그럼 테케랑 다를텐데.. 
    while wolf:
        x,y = wolf.popleft() # 늑대의 위치 
        for i in range(4):
            #늑대의 위치에서 동서남북
            nx = dx[i] + x 
            ny = dy[i] + y

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == ".":
                #. 위치에서 동서남북
                Nx = dx[i] + nx
                Ny = dy[i] + ny
                if 0 <= Nx < R and 0 <= Ny < C : 
                    if graph[Nx][Ny] == "S": #근처에 양이 있다면 
                        graph[nx][ny] = "D" # 울타리 놓기 

# 늑대가 양에게 도달할 수 있는지 확인하는 함수             
def dfs(x,y):
    # grpah 에 아예 'w'가 없는 경우 
    # 배열 다 탐색하도고 없으면 1출력 
    # 늑대가 양에게 갈 수 있는지 확인 
    visited[x][y] = True
    for i in range(4):
        nx = dx[i] + x 
        ny = dy[i] + y
        if 0 <= nx < R and 0 <= ny < C :
            if graph[nx][ny] != 'D':
                continue
            elif graph[nx][ny] == 'W':
                dfs(nx,ny)
            elif graph[nx][ny] == '.':
                continue
            else:
                return "0"
        
    return "1"



wolf = deque()

R,C = map(int,sys.stdin.readline().split())
graph = [ list(sys.stdin.readline()) for _ in range(R)]
visited = [[False] * C for _ in range(R)] 
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'W':
            wolf.append((i,j))
            bfs(i,j)

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'W':
            print(dfs(i,j))
            

print("\n".join(map("".join,graph)))
'''

# 아.. 문제에서 울타리를 최소로 놓으라고 한적 없으니까 테스트케이스랑 달라도 되네...
# 그래도 접근하려했던 나의 노력을 칭찬해,,^^,,

import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력
R, C = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(R)]

wolf = deque()

# 모든 늑대(W) 위치 큐에 저장
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'W':
            wolf.append((i, j))

# 늑대(W) 주변에 울타리(D) 설치
for x, y in list(wolf):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] == "S":  # 늑대가 양 근처에 있으면 0 출력 후 종료
                print(0)
                exit()
            if graph[nx][ny] == ".":  # 늑대 주변 빈칸을 울타리로 변경
                graph[nx][ny] = "D"

# 예제 출력처럼 양(S) 주변에도 울타리 추가
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] == ".":
                    graph[ni][nj] = "D"

# 결과 출력
print(1)
print("\n".join("".join(row) for row in graph))

