import sys 

N,K = map(int,sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
coins.sort(reverse=True)

count =0
for i in range(N):
    if coins[i] <= K :
        count += K//coins[i]
        K = K % coins[i]
        #print(f"K = {K}, count = {count}")
    if K == 0:
        break

print(count)
