import sys
N,K = map(int,sys.stdin.readline().split())
lans = [int(sys.stdin.readline()) for _ in range(N)]

def solutions():
    
    start = 1 # 랜선의 최소 길이(start) 
    end = max(lans) # 랜선의 최대 길이
    answer = 0
    # 최대값은 해당하는 값보다 작은 값들은 모두 조건을 만족해야한다.
    # 만약 조건을 만족하지 않는 경우, 탐색 하는 범위는 작은값에서 탐색해야한다. 
    
    while start <= end:
        mid = (start+end)//2
        lan =0
        for i in lans:
            lan += i//mid 
        
        if lan >= K:
            start = mid + 1 # 더 긴 랜선으로 자를 수 있는지 확인 

        else:
            end = mid -1 # 랜선이 너무 길어서 부족한것이므로, 더 짧은 길이의 랜선으로 랜선 개수를 맞출 수 있는지 확인 
        
    print(end)

solutions()