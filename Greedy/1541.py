# 식의 값을 최소로 

import sys

# -를 기준으로 나눈다. 
N = sys.stdin.readline().strip().split('-')
#print(N)

for i in range(len(N)):
    N[i] = sum(map(int,N[i].split('+'))) # 이거 .. 잘 생각해야만.. 생각안난다.
    #print(N[i])

num =0
for i in range(1,len(N)):
    N[i-1] -= N[i]

print(N[0])





