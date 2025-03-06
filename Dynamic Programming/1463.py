

#진짜모르겟음 풀이 한번 보고 나중에 다시 풀어보자.

'''
점화식

dp[2] = dp[1]+1
기본적으로 -1 연산 : dp[i] = dp[i-1]+1
i 가 2 나떨 : dp[i] = min(dp[i],dp[i//2]+1)
i 가 3 나떨 : dp[i] = min(dp[i],dp[i//3]+1)


dp는 미리 값을 다 채워두고 그거에 맞게 연산하면 되는것같음
'''
import sys
def min_operations(N):
    dp = [0] * (N+1)

    for i in range(2,N+1):
        #기본적으로 -1연산 사용하는 경우
        dp[i] = dp[i-1]+1
    
        if i%2 == 0:
            # 앞서 채워놓은 -1 보다 작은값이 나오는지
            dp[i] = min(dp[i],dp[i//2]+1)
        
        if i%3 ==0:
            dp[i] = min(dp[i],dp[i//3]+1)
    
    return dp[N]

N = int(sys.stdin.readline().strip())
print(min_operations(N))
