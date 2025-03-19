import sys 
from collections import deque
# 3초 이후 폭발 
# 인접한 네칸이 폭발함 
# 폭탄설치 -> 2초때 폭탄 설치 -> 3초때 맨 처음 설치한 폭탄이 폭발함




dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bomb():
    cnt = 1
    while cnt < N :
        print("현재 cnt 값 : ", cnt)
        cnt +=1

        
        if cnt % 2 == 1 : #홀수면 
        # 폭탄의 위치를 저장해둔걸 기반으로 주변 폭탄 터뜨림 
            for x,y in list(Bombq):
                Arr[x][y] = "."
                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y 
                    
                    if 0<=nx<R and 0<=ny<C :
                        if Arr[nx][ny] == "O":
                            Arr[nx][ny] = "."

        elif cnt % 2 == 0 : #짝수면
        # 폭탄이 설치되지 않은 모든 칸에 폭탄을 설치함 
            # 모든 노드 탐색해서 0 아닌곳은 다 0 만들어버리고 폭탄 위치 저장
            for i in range(R):
                for j in range(C):
                    if Arr[i][j] == ".":
                        print("현재 cnt 값 : ", cnt)
                        Bombq.append((i,j))
                        Arr[i][j] = 'O'
                        

Bombq = deque()
R,C,N = map(int,sys.stdin.readline().split())
Arr = [list(sys.stdin.readline().strip()) for _ in range(R)]


# 처음 폭탄의 위치를 저장해둔다.
for i in range(R):
    for j in range(C):
        if Arr[i][j] == 'O':
            Bombq.append((i,j))


if N ==1 :
    print("\n".join("".join(row) for row in Arr))
else:
    bomb()
    print("\n".join("".join(row) for row in Arr))

# N 초가 될때까지 격자판탐색을 진행해야한다. 
# N ==1 일때는 맨 처음 상태 그대로 출력 
# N%2 == 0 일때는 폭탄이 설치되지않은 모든 칸에 폭탄을 설치
# N % 2 == 1일때에 폭탄이 폭발 

'''
0 : 폭탄 설치
1 : 아무것도 안함
2 : 폭탄 설치
3 : 폭탄 폭발
4 : 폭탄 설치
5 : 폭탄 폭발
6 : 폭탄 설치
7 : 폭탄 폭발
8 : 폭탄 설치
9 : 폭탄 폭발 

'''



'''
내 코드에서 잘못된 점 

'''