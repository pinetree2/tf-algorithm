# 맥주 마시면서 걸어가기
# import sys

# def beer_feel(arr):
#   for i in range(1,len(arr)):
#     x1, y1 = arr[i-1]
#     x2, y2 = arr[i]
#     distance = abs(x2-x1) + abs(y2-y1)
#     if distance/50 > 20:
#         print("sad")
#         exit()
#     elif distance/50 <= 20:
#         continue

#   print("happy")



# t = int(sys.stdin.readline())

# for _ in range(t):
#   n = int(sys.stdin.readline())
  
#   # 상근이 좌표 입력받기
#   # n 만큼 편의점 좌표 입력받기
#   # 펜타포스트 좌표 입력받기
#   arr = []
#   for _ in range(n+2):
#     x, y = map(int, sys.stdin.readline().split())
#     arr.append((x,y))
#   # 탐색 함수 호출 
#   beer_feel(arr)
  
### 개선한 코드

# 맥주 마시면서 걸어가기
import sys
from collections import deque

def beer_feel():
  q = deque()
  q.append((start_x,start_y))
  while q:
    x,y = q.popleft()
    if abs(x-end_x)+abs(y-end_y) <= 1000:
      print("happy")
      return 
    for i in range(n):
      if not visited[i]:
        nx,ny = arr[i]
        if abs(nx-x)+abs(ny-y) <= 1000:
          visited[i] =1
          q.append((nx,ny))
        
  print("sad")
  return


t = int(sys.stdin.readline())

for _ in range(t):
  n = int(sys.stdin.readline())
  start_x,start_y = map(int,sys.stdin.readline().split())
  # 상근이 좌표 입력받기
  # n 만큼 편의점 좌표 입력받기
  # 펜타포스트 좌표 입력받기
  arr = []
  for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x,y))
  # 탐색 함수 호출 
  end_x,end_y = map(int,sys.stdin.readline().split())
  visited = [0 for _ in range(n+1)]
  beer_feel()





