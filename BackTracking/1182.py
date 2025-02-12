# 아 하기싫다 . . . . 

import sys 

def dfs(index, sum):
    global count
    if index > 0 and sum == S:
        count += 1
    for i in range(index,N):
        #print("i: ",i,"index: ",index,"sum: ",sum)
        dfs(i+1, sum+arr[i])
        
            

N,S = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
count = 0

dfs(0,0)
print(count)