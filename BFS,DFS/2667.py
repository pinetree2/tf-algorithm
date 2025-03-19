import sys 


# 각 단지의 개수 ...구해야하는데,, 
# dfs 이용해야할듯, 주변에 1 있으면 파고파고.., 방문하면 0으로 바꾸고 
# 더이상 1이 존재하지 않는다면 끝내고..
# 단지[0] = 집 개수 요런식으로 해야하지 않을까? 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# dfs 이용 
def Home(x,y):
    #print("cnt값:", cnt)
    visited[x][y] = True
    cnt = 1

    for i in range(4):
        nx,ny = dx[i]+x, dy[i]+y
        if 0<=nx<N and 0<=ny<N and Homes[nx][ny] == 1 and not visited[nx][ny]:
            cnt +=Home(nx,ny)
    return cnt 



N = int(sys.stdin.readline())
Homes = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
answer = []

for i in range(N):
    for j in range(N):
        #print("Homes[i][j]값:",Homes[i][j])
        if Homes[i][j] == 1 and not visited[i][j]:            
            answer.append(Home(i,j))

answer.sort()
print(len(answer))
# for i in range(len(answer)):
#     print(answer[i],sep=" ")
print("\n".join(map(str, answer)))