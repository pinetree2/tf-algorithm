import sys
N,K = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# 말의 정보는 세개의 정수 행, 열 번호, 이동방향(r,c,d )
horse = [list(map(int,sys.stdin.readline().split())) for _ in range(K)]

# 행과 열의 정보는 1부터 시작이라서 체스판에 맞추려면 -1 해야함
# 이동방향은 1,2,3,4 (우 좌 상 하)


def white(horse_position, r,c):
  # 말의 위치 정보를 담는 2차원 리스트 (스택 사용)
  if not horse_position[r-1][c-1]:  
    # 해당 위치에 말이 없다면 
    horse_position[r-1][c-1].append(i)  # 말의 순서를 추가 (스택에 push)
  else:  # 해당 위치에 말이 이미 있다면
        horse_position[r-1][c-1].append(i)  # 말의 순서를 추가 (스택에 push)
  return horse_position


def red(horse_position, r,c):
  # 말이 이미 존재하는지 확인 후 순서 반대로 변경
  if not horse_position[r-1][c-1]:
    horse_position[r-1][c-1].append(i)

  else:
      horse_position[r-1][c-1].append(i)  # 말의 순서를 추가 (스택에 push)
      # 순서를 반대로 변경
      horse_position[r-1][c-1].reverse()
  return horse_position

turn = 0
# 말의 위치를 저장하는 배열 생성
horse_position = [[[] for _ in range(N)] for _ in range(N)]  
game_over = False
# 게임 시작
while not game_over:
  turn +=1
  if turn > 1000:
    print(-1)
    break
  
  # 말의 정보를 가져온다.
  for i in range(K):
    r,c,d = horse[i]

    if d == 1: # 오른쪽, 열+1
      # d 에 맞게 r,c 값 변경
      r,c = r,c+1
      # 지금 여기에 배열 크기를 넘어갔을때의 처리가 없음, blue 와 같이 방향변경만 해주면됨 4,0(N보다커진) / -1,0(0보다 작아진) / 0,4 (N보다 커진/ 0,-1 (0보다 작아진)/
      if c > N:
        c = N
        d = 2
        horse[i] = [r,c,d]
        continue
      if arr[r-1][c-1] == 0:
        if len(horse_position[r-1][c-1]) == 4:
          game_over = True
          break
        horse_position = white(horse_position,r,c)
      if arr[r-1][c-1] == 1:
        if len(horse_position[r-1][c-1]) == 4:
          game_over = True
          break
        horse_position = red(horse_position,r,c)

      if arr[r-1][c-1] == 2 :
        d = 2
        r,c = r,c-1
        if c < 0:
          c = 0
          d = 1
          horse[i] = [r,c,d]
          continue 
        if arr[r-1][c-1] == 0:
          if len(horse_position[r-1][c-1]) == 4:
            game_over = True
            break
          horse_position = white(horse_position,r,c)
        elif arr[r-1][c-1] == 1:
          if len(horse_position[r-1][c-1]) == 4:
            game_over = True
            break
          horse_position = red(horse_position,r,c)
        else:
          c = c+1
          horse[i] = [r,c,d]
    
    if d == 2: # 왼쪽, 열 -1
      # d 에 맞게 r,c 값 변경
      r,c = r,c-1
      if c < 0:
        c = 0
        d = 1
        horse[i] = [r,c,d]
        continue 
        
      if arr[r-1][c-1] == 0:
        if len(horse_position[r-1][c-1]) == 4:
          game_over = True
          break
        horse_position = white(horse_position,r,c)

      if arr[r-1][c-1] == 1:
        if len(horse_position[r-1][c-1]) == 4:
          game_over = True
          break
        horse_position = red(horse_position,r,c)

      if arr[r-1][c-1] == 2 :
        d = 1
        r,c = r,c+1
        if c > N:
          c = N
          d = 2
          horse[i] = [r,c,d]
          continue
        if arr[r-1][c-1] == 0:
          if len(horse_position[r-1][c-1]) == 4:
            game_over = True
            break
          horse_position = white(horse_position,r,c)
        elif arr[r-1][c-1] == 1:
          if len(horse_position[r-1][c-1]) == 4:
            game_over = True
            break
          horse_position = red(horse_position,r,c)
        else:
          c = c-1
          horse[i] = [r,c,d]
      
    if d == 3:
      # d 에 맞게 r,c 값 변경
      r,c = r-1,c
      if r < 0:
        r = 0
        d = 4
        horse[i] = [r,c,d]
        continue 
      if arr[r-1][c-1] == 0:
        if len(horse_position[r-1][c-1]) == 4:
          game_over = True
          break
        horse_position = white(horse_position,r,c)

      if arr[r-1][c-1] == 1:
        if len(horse_position[r-1][c-1]) == 4:
          game_over = True
          break
        horse_position = red(horse_position,r,c)

      if arr[r-1][c-1] == 2 :
        d = 4
        r,c = r+1,c
        if r > N:
          r = N
          d = 3
          horse[i] = [r,c,d]
          continue
          
        if arr[r-1][c-1] == 0:
          if len(horse_position[r-1][c-1]) == 4:
            game_over = True
            break
          horse_position = white(horse_position,r,c)
        elif arr[r-1][c-1] == 1:
          if len(horse_position[r-1][c-1]) == 4:
            game_over = True
            break
          horse_position = red(horse_position,r,c)
        else:
          # 방향만 바꾸고 이동 x 
          r = r-1
          horse[i] = [r,c,d]

    if d == 4:
      # d 에 맞게 r,c 값 변경
      r,c= r+1,c
      if r > N:
        r = N
        d = 3
        horse[i] = [r,c,d]
        continue
        
      if arr[r-1][c-1] == 0:
        if len(horse_position[r-1][c-1]) == 4:
          game_over = True
          break
        horse_position = white(horse_position,r,c)

      if arr[r-1][c-1] == 1:
        if len(horse_position[r-1][c-1]) == 4:
          game_over = True
          break
        horse_position = red(horse_position,r,c)

      if arr[r-1][c-1] == 2 :
        d =3
        r,c = r-1,c
        if r < 0:
          r = 0
          d = 4
          horse[i] = [r,c,d]
          continue 
        if arr[r-1][c-1] == 0:
          if len(horse_position[r-1][c-1]) == 4:
            game_over = True
            break
          horse_position = white(horse_position,r,c)
        elif arr[r-1][c-1] == 1:
          if len(horse_position[r-1][c-1]) == 4:
            game_over = True
            break
          horse_position = red(horse_position,r,c)
        else:
          r = r+1
          horse[i] = [r,c,d]
  if game_over:
    print(turn)
    break
  