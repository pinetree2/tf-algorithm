import sys
N,K = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 말의 정보는 세개의 정수 행, 열 번호, 이동방향(r,c,d )
horse = [list(map(int,sys.stdin.readline().split())) for _ in range(K)]

# 행과 열의 정보는 1부터 시작이라서 체스판에 맞추려면 -1 해야함
# 이동방향은 1,2,3,4 (우 좌 상 하)

turn = 0
# 게임 시작
while True:
  turn +=1
  if turn > 1000:
    break

  # 만약 말이 도저히 4개로 합쳐질 수 없다면 return -1
  # 이건 또 어케알지요 

  
  # 말의 정보를 가져온다.
  for i in range(K):
    r,c,d = horse[i]
    # 근데 이 말의 위치가 겹칠 경우에는 순서를 어디에 담아야하는지를 모르겠음, 따로 담아야 하나? 근데 그러면그때마다 확인을 해야해? 어카지? NxN 배열에 말의 순서를 담는 배열을 따로 만들어야 하나?
    
    # 이동 하려는 칸이 흰색 
    if arr[r-1][c-1] == 0:
      # 말의 위치 이동
      # direction 확인
      if d == 1:
        # d 에 맞게 r,c 값 변경
      if d == 2:
        # d 에 맞게 r,c 값 변경
      if d == 3:
        # d 에 맞게 r,c 값 변경
      if d == 4:
        # d 에 맞게 r,c 값 변경

      # 말이 이미 존재하는지 확인 후 순서 변경 
        #체스판을 벗어나려는 경우 방향만 바꿔준다.

    # 이동하려는 칸이 빨간색 
    elif arr[r-1][c-1] == 1:
      # 말의 위치 이동
      # direction 확인
      if d == 1:
        # d 에 맞게 r,c 값 변경
      if d == 2:
        # d 에 맞게 r,c 값 변경
      if d == 3:
        # d 에 맞게 r,c 값 변경
      if d == 4:
        # d 에 맞게 r,c 값 변경

      # 말이 이미 존재하는지 확인 후 순서 반대로 변경 
        #체스판을 벗어나려는 경우 방향만 바꿔준다.

    # 이동 하려는 칸이 파란색 
    elif arr[r-1][c-1] == 2:
      # 말의 위치 이동
      # direction 확인 후 방향을 반대로 변경 
      # 파란색은 방향변경만 하고 이동은 다른 곳에서 할 수 없나?
      # direction에 맞게 이동
        # 만약 이때 이동하려는 칸이 또 파란색이라면 방향만 또 변경

      #체스판을 벗어나려는 경우 방향만 바꿔준다.
      
      
    
      
      
      