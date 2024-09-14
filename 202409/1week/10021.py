import sys 
N,C = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dist = [[0]*N for _ in range(N)]

answer = 0

# 각 노드간의 비용 구하기
# 비용 : (xi - xj)^2 + (yi - yj)^2

# dist[i][j] 가 C 이상이면서, 최소의 값인지를 확인
for i in range(N):
  for j in range(i+1,N):
    distance = (graph[i][0] - graph[j][0])**2 + (graph[i][1] -graph[j][1])**2
    # 이미 dist[i][j] 에 값이 존재하지 않는 경우에만
    if not dist[i][j]:
      dist[i][j] = dist[j][i] = distance
      
    if dist[i][j] >= C:
      # dist[i][j] 보다 작은 값이 있는지 확인
      min_dist = dist[i][j]
      for k in range(i+1,N):
        if dist[i][k] >= C and dist[i][k] < min_dist:
          min_dist = dist[i][k]
      # dist[i][j] 가 최소값이면 answer 에 더함
      if min_dist == dist[i][j]:
        answer += dist[i][j]
print(answer)