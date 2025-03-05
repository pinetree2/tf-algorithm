'''
dp [i] = dp[i-3] +1 or dp[i-5]+1


n = 18  (3kg, 5kg만 사용 가능)

dp[3] = 1  (3kg 1봉지)
dp[5] = 1  (5kg 1봉지)

dp[6] = dp[3] + 1 = 2  (3kg 2봉지)
dp[9] = dp[6] + 1 = 3  (3kg 3봉지)
dp[10] = dp[5] + 1 = 2 (5kg 2봉지)

dp[15] = dp[10] + 1 = 3  (5kg 3봉지)
dp[18] = dp[15] + 1 = 4  (5kg 3봉지 + 3kg 1봉지)

'''
import sys

n = int(sys.stdin.readline())
dp = [-1] * 5001  # -1로 초기화 (기본적으로 만들 수 없는 상태)
dp[0] = 0  # 0kg은 봉지 0개 필요
if n >= 3:
    dp[3] = 1  # 3kg은 봉지 1개
if n >= 5:
    dp[5] = 1  # 5kg은 봉지 1개

for i in range(6, n + 1):  # 6kg부터 n까지 DP 계산
    if dp[i - 3] != -1:  # 3kg을 뺀 경우가 가능하면
        dp[i] = dp[i - 3] + 1
    if dp[i - 5] != -1:  # 5kg을 뺀 경우가 가능하면
        # 이미 dp[i]가 갱신된 경우 최소값 비교
        if dp[i] == -1:  # 아직 갱신되지 않았다면
            dp[i] = dp[i - 5] + 1
        else:  # 이미 갱신된 값이 있다면 최소값 선택
            dp[i] = min(dp[i], dp[i - 5] + 1)

print(dp[n])

# 다시 풀자~~
# 사실 그리디로도 충분히 가능함 