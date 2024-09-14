import sys
H,W,X,Y = map(int,sys.stdin.readline().split())
# 행 : 높이 , 열 : 너비 헛갈려죽겄어
A = [[0]*W for _ in range(H)]
# 행의 개수를 알고있어서 가능한 입력 
B = [list(map(int,sys.stdin.readline().split())) for _ in range(H+X)]

# A[X][Y] 부터 겹치게된다.
# B배열을 돌면서, B[X][Y] 까지는 안겹치니까 값을 A 에 넣어준다.
for i in range(H):
  for j in range(W):
    if i <= X or j < Y:
      A[i][j] = B[i][j]
        

# A[X][Y] 부터는 값을 B 를 이용하여 찾아야 한다.
for i in range(H):
  for j in range(W):
    if i >= X and j >= Y:
      A[i][j] = B[i][j] - A[i-X][j-Y]
      

# A 배열을 리턴 
for i in A:
  for j in i:
    print(j,end=' ')
  print()