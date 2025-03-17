import sys 

cnt = 0 # M을 만족하는 부분 수열 개수 
N,M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
i,j = 0,0
sumResult =0 #현재 부분합 

while j<N:
    #sumResult =0
    sumResult += A[j] # j 위치의 값을 더한다. 
    j += 1 # j 값 증가 

    while sumResult >= M:  # 합이 M 이상이면 i를 증가시키면서 조정
        if sumResult == M:  # 부분합이 정확히 M이면 카운트 증가
            cnt += 1
        sumResult -= A[i]  # i 위치의 값을 제거
        i += 1  # i 증가

    # if i < j: 
    #     sumResult = sum(A[i:j+1]) #이게 아닌가 .. 
    #     if sumResult == M:
    #         cnt +=1  
    #         i+=1
    #         j = i+1
    #     else:
    #         j = i+1

print(cnt)
    

