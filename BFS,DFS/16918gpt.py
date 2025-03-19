import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def simulate():
    global Arr
    # 폭탄이 터질 위치 저장
    explode_positions = set()

    # 기존 폭탄들의 위치 저장
    for i in range(R):
        for j in range(C):
            if Arr[i][j] == 'O':
                explode_positions.add((i, j))

    # 전체를 폭탄으로 채우기 (폭발 전 상태)
    Arr = [['O'] * C for _ in range(R)]

    # 폭탄 폭발 처리
    for x, y in explode_positions:
        Arr[x][y] = '.'  # 본래 폭탄 터짐
        for i in range(4):  # 상하좌우도 터짐
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                Arr[nx][ny] = '.'  # 연쇄 폭발

# 입력 처리
R, C, N = map(int, sys.stdin.readline().split())
Arr = [list(sys.stdin.readline().strip()) for _ in range(R)]

if N == 1:
    # 1초면 초기 상태 그대로 출력
    print("\n".join("".join(row) for row in Arr))
elif N % 2 == 0:
    # 짝수 초에는 무조건 모든 칸에 폭탄이 가득 참
    print("\n".join("O" * C for _ in range(R)))
else:
    # 홀수 초(N이 3 이상이면서 홀수)
    simulate()  # 3초 상태로 만들기
    if N % 4 == 3:
        # N이 3, 7, 11, ... 인 경우, 폭발 1회 상태 유지
        print("\n".join("".join(row) for row in Arr))
    else:
        # N이 5, 9, 13, ... 인 경우, 폭발 2회 상태 (simulate() 한 번 더 실행)
        simulate()
        print("\n".join("".join(row) for row in Arr))
