import sys
N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

dp = [1] * N

for i in range(1,N):
    for j in range(i):
        if card[i] > card[j]: # 이전 원소가 현재 원소보다 작다면,(이전원소들 모두 보는거)
            dp[i] = max(dp[i],dp[j]+1)

answer = max(dp)
print(answer)

# 다 방문하면서 값을 비교하며 인덱스별 dp값을 갱신해주는 