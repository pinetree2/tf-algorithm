import sys 
# 두 수를 골랐을 때, 그 차이가 M이상이면서 제일 작은 경우

N,M = map(int,sys.stdin.readline().split())
A = [int(sys.stdin.readline().strip()) for _ in range(N)]
i,j = 0,0
A.sort()

# 정렬했으니까 i,j 증가 잘 지켜봅세 
min_diff = float('inf')  # 최소 차이 초기화 min_diff를 가장 작은 값으로 갱신해야 합니다.
#처음에는 아무 값도 없으므로, 충분히 큰 값으로 초기화해야 합니다.
while  j<N and i<N:
    sub = A[j] - A[i]
    if sub >= M:
        min_diff = min(min_diff,sub) #작은값을 넣어야징
        i+=1 #더 작은값 찾기위해 i 증가 
    else:
        j+=1 # M보다 작으면 j 증가 ( 더 큰 값 탐색 )

print(min_diff)