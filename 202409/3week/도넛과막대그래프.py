

def solution(edges):

    answer = [0,0,0,0]
        # 주어진 간선에서 등장하는 최대 정점을 구함
    max_node = max(max(x, y) for x, y in edges)
    
    # 방문 배열을 간선에 등장하는 최대 정점까지만 할당
    visited = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)]
    for x,y in edges:
        if visited[x][y] != True:
            dfs(x,y,visited,edges)

    # 어떤 그래프인지 방문배열을 통해 확인해보자.
    # 0. 시작 정점인 경우 -> visited[x][?] , visited[?][x] 인 경우가 없는 경우 + visited[x][?] 의 경우가 2개 이상인 것
    # 1. 막대 그래프인 경우 -> visited[x][?] , visited[?][x] 인 경우가 없는 경우 
    # 2. 도넛 그래프인 경우 -> visited[x][?] , visited[?][x] 인 경우가 한개만 있는 경우
    # 3. 8자 그래프인 경우 -> visited[x][?] , visited[?][x] 인 경우가 두개 이상인 경우

    cnt = 0
    for i in range(1, max_node + 1):
        for j in range(1, max_node + 1):
            if visited[i][j] == True and visited[j][i] == True:
                print(i,j)
                cnt +=1
            else: 
                count_x = sum(visited[i])  # visited[i][?]가 True인 경우의 수를 셈
                if count_x >= 2:
                    answer[0] = i
        if cnt == 0:
            answer[2] +=1
        elif cnt == 1:
            answer[1] +=1
        else:
            answer[3] +=1

    return answer

def dfs(s,d, visited, edges):
        if visited[s][d]:
            return
        visited[s][d] = True
        for x,y in edges:
            if x == d and not visited[d][y]: # x 는 곧 d 가 되므로 시작 정점을 d로 변경해서 새로 dfs ㄱㄱ
                dfs(d,y, visited, edges)



