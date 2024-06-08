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

'''
def bfs(x,y,arr):

# 0 이면 반복문 ㄱㄱ , distance +=1

# 1 이면 빽하고 다른 방향으로 

# 2,3,4 라면 찾았으니 distance 를 return한다, exit.


'''

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