import sys 
sys.setrecursionlimit(100000)  # 재귀 깊이 문제 방지


# 대각선으로만 인접된것은 뭉쳐있다고 보지 않는다. 
# 떨어져있는 그룹은 다른 그룹인데 이걸 어떻게.. 
def dfs(x,y):
    visited[x][y] = True
    color = graph[x][y]
    cnt = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == color:
            cnt += dfs(nx,ny)
    return cnt

N,M = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(M)]
# B는 파랑, W는 흰색
visited = [[False] * N for _ in range(M)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
B_cnt=W_cnt = 0

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            size = dfs(i,j)
            power = size ** 2
            if graph[i][j] == 'W':
                W_cnt += power
            elif graph[i][j] == 'B':
                B_cnt += power

print(W_cnt,B_cnt)

# 아 ~ 거의 다 풀었는데 항상.. 응용을 못함 