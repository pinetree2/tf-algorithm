import sys
N,S = map(int,sys.stdin.readline().split())
Arr = list(map(int,sys.stdin.readline().split()))

min_length = 100000
sum = 0
start,end = 0,0

while True:
    if sum >= S:
        min_length = min(min_length,end-start)
        sum -= Arr[start]
        start +=1
    elif end == N:
        break
    else:
        sum += Arr[end]
        end +=1

if min_length == 100000:
    print(0)
else:
    print(min_length)

