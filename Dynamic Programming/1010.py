'''
DP 가 적용되기 위해서는 2가지 조건이 필요하다.
- 겹치는 부분 문제 : 문제를 작은 문제로 나누고, 작은 문제의 결과를 재사용해서 원하는 결과를 도출하는 과정
- 최적 부분 구조 :소문제들의 최적 결과 값을 이용해 전체 문제의 최적 결과를 낼 수 있는 경우에 DP를 적용할 수 있다. 

'''

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
