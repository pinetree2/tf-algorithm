import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())
MAX = 100001
visited = [0] * MAX

def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x])
            return 
        for i in [x-1,x+1,x*2]:
            if 0 <= i < MAX and not visited[i]:
                visited[i] = visited[x] + 1 #방문 횟수
                queue.append(i)
        
bfs()     

'''
1초 : 2*5(X) = 10
2초 : 10-1 = 9
3초 : 2*9(X) = 18
4초 : 18-1 = 17

최적의 경로를 찾는 문제 -> BFS 


그럼 6,19
6 -> 12
12 -> 24
24 - 5 = 19 

'''



