import sys 

'''
dp[n] = dp[n-1] + dp[n-2]
'''

n = int(sys.stdin.readline())
dp = [0] * (n+2)
dp[0] = 0
dp[1] =1
for i in range(2,n+2):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])

