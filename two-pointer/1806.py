import sys 
N,S = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
i,j =0,0

min_length = float("inf")
Sum = 0
result = 0
# 부분합이 S 이상이 되어야 하고, 가장 짧아야 함 
# 아오 2030,2230,이 문제까지 다 비슷한데 해결을 못하네..

while i < N and j <N :
    #Sum = sum(arr[i:j])
    Sum += arr[j] # j 위치의 값을 추가 
    j +=1 # j 증가
    #if Sum >= S :
    while Sum >= S : # 조건을 만족하면 i를 이동하며 최소 길이 갱신 
        #min_diff = min(min_length,Sum)
        # if min_diff == S :
        #     result = j-i+1
        min_length = min(min_length,j-i)
        Sum -= arr[i] # i 위치의 값을 제거 
        i+=1
    else:
        j+=1

print(min_length if min_length != float("inf") else 0)

# 이게 슬라이딩 윈도우래 

'''
기존 내 코드는 sum함수를 매번 호출해서 시간 복잡도가 너무 높아졌음
슬라이딩 윈도우 방식으로 sum을 업뎃한다.
부분합이 S이상이 되었을 때 i를 업데이트 한다.
j만 먼저 움직여서 합 구하는거 
'''