

import sys
from collections import deque


def bfs(start):

    queue = deque([start])
    #visited[start] = True
    time[start] = 0  # 시작 위치의 시간은 0으로 초기화
   
    while queue:
        v = queue.popleft()
        print("\n현재 v",v)
        
        if v == K:
            return time[v]
        
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and time[i] == -1:
                print("\n현재 i",i)
                #visited[i] = True
                if i == 2*v:
                    queue.appendleft(i) #순간이동이 비용 0초이므로 deque.appendleft(i)를 사용하여 큐의 앞에 추가
                    print("\n현재 queue",queue)
                    time[i] = time[v]
                    print("\n현재 time",time[i])
                else:
                    queue.append(i)
                    print("\n 현재 queue",queue)
                    time[i] = time[v] + 1
                    print("\n 현재 time",time[i])
            if i == K:
                return time[K]
        
        

N,K = map(int,sys.stdin.readline().split())
#visited = [False] * 100001  # 방문 여부를 기록
time = [-1] * 100001 #방문배열 겸 시간 체크 
print(bfs(N))




'''

수빈이의 위치 X , 1초후에는 X-1 혹은 X+1 로 이동, 
순간이동시 2*X로 이동 (0초, 시간 증가 안함)
수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 출력
최대한 순간이동을 많이 해야겠는디? 

5 -> 4,6,10 (0초)
10 -> 11,9,20 (1초)
9 -> 8,10,18 (0초)
18 -> 17,19,36 (1초)

하나의 노드당 인접노드가 3개씩 존재.
이동시간은 0초 혹은 1초
모든 인접 노드중에 가장 빠른 시간을 찾으면 되는데
이전에 계산한 time 과 새로 탐색한 경로의 time 을 비교해서 제일 짧은 시간을
리턴하면 되지않을까?

time 비교는 어떻게 해야하지?

---
처음에 런타임 에러 발생했다.
이는 i의 수를 확인하지 않아서였다. 아마 무한루프가 발생했을 것이다.
그리고, 방문 배열을 만들지 않고, time 배열을 만들어서 방문했는지 여부를 체크하였다.

queue.appendleft(i) 를 사용하여 큐의 앞에 추가하는 방법을 사용하였다.
그럼 순간이동 하는 노드들을 제일 먼저 다 돌고
그 다음에 일반 이동하는 노드들을 돌게 된다.
그럼 순간이동을 최대한 많이 할 수 있게 된다.

'''