'''
DP 가 적용되기 위해서는 2가지 조건이 필요하다.
- 겹치는 부분 문제 : 문제를 작은 문제로 나누고, 작은 문제의 결과를 재사용해서 원하는 결과를 도출하는 과정
- 최적 부분 구조 :소문제들의 최적 결과 값을 이용해 전체 문제의 최적 결과를 낼 수 있는 경우에 DP를 적용할 수 있다. 


import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    
import sys
input = sys.stdin.readline

def bridge(n, m):
  dp = [[0 for _ in range(m+1)] for _ in range(n+1)] 
  
  for i in range(1, m+1): dp[1][i] = i # N = 1일 때

  # N이 2 이상일 때 
  for i in range(2, n+1): 
    for j in range(i, m+1):
      for k in range(j, i-1, -1):
        dp[i][j] += dp[i-1][k-1]

  return dp[n][m]

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  print(bridge(N,M))
#https://kau-algorithm.tistory.com/780
#다음에 다시 보자.



'''

# 다시 풀어욤

import sys

'''
N=1 --> M
N=2 --> 1+..+M-1
N=3 --> 1+..+M-2
N=4 --> 1+..+M-3
..
N == M -> 1

이기도 하고,,
(M-N+1)+ ..+1 이 경우의 수임 

dp[2][4] = dp[4][4]+dp[3][4]
이고,
dp[2][5] = dp[5][5] + dp[4][5] +dp[3][5] 

dp[2][5] = dp[2][4] + dp[1][4] 이기도 함!! 
'''

def bridge(N,M):
  # 이.. dp 배열을 쓰는게 너무 어려움 
  dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

  # N = 1 일때 값은 M
  for i in range(1,M+1):
      dp[1][i] = i
    
  # N이 2 이상일 때
  for i in range(2,N+1):
      for j in range(i,M+1):
          # n = j-i+1
          # dp[i][j] += ((n * (n+1)) //2)
          dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
  
  return dp[N][M]

T = int(sys.stdin.readline())
for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    print(bridge(N,M))


