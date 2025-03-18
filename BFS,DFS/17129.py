#윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유 
import sys 
from collections import deque



# 출발지점 : 2의 위치 
# 0 이아닌 숫자를 만나는 그 순간의 거리중 가장 짧은 것 
# 1은 장애물이라 지나갈수 없음 

# 방향 
dx = [ -1, 1, 0,0]
dy = [0,0,-1,1]

def bfs(x,y,distance):
    queue = deque([(x,y,distance)])
    visited[x][y] = True
    #큐가빌때까지
    while queue:
        a,b,distance = queue.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
        
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] and A[nx][ny] != 1 :
                    visited[nx][ny] = True
                    queue.append((nx,ny,distance+1))
                    if A[nx][ny] in [3,4,5]:
                        print(f"TAK\n{distance+1}")
                        return
    
    print("NIE")



# 음식 빨리 도착 -> BFS 
n,m = map(int,sys.stdin.readline().split())
A = [list(map(int, list(input()))) for _ in range(n) ]
visited=[[False] * m for _ in range(n)] 
#print(A)
#print(n,m)
#print(A)
# 2의 위치에서 시작
for i in range(n):
    for j in range(m):
        if A[i][j] == 2:
            bfs(i,j,0)
            A[i][j] = 1

            


# 58분소요 
# 시간초과 이슈..

'''
이코드는 시간초과 안났는데,, 차이점이 뭐지
# 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유 : 제목 너무 웃기다.

import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

# n,m의 크기를 가진 matrix 입력
arr = [list(map(int, list(input()))) for _ in range(n)]

# 일단 방향배열 선언 
# 위 아래 왼 오
dx = [-1,1,0,0]
dy = [0,0,-1,1]

dq = deque()

# 배열에서 2가 있는 위치를 저장해둔다.
for i in range(n):
  for j in range(m):
    if arr[i][j] == 2:
      dq.append((i,j,0)) #딱따구리 위치, 거리
      arr[i][j] = 1



while dq:
  x,y,dis = dq.popleft()
  for d in range(4):
    nx = x+dx[d]
    ny = y+dy[d]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
      continue 
    if arr[nx][ny] == 1:
      continue 
    if arr[nx][ny] in [3,4,5]:
      print("TAK")
      print(dis+1)
      exit()
    dq.append((nx,ny,dis+1))
    arr[nx][ny] = 1

print("NIE")

'''