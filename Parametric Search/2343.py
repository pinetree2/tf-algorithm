# 블루레이의 크기를 최소로, M개의 블루레이는 모두 같은 크기
# 최대한 블루레이의 크기를 줄이는게 목표 , 최댓값중 최소값을 구해야함 
# 아까 그 골드문제다....

import sys 

N,M = map(int,sys.stdin.readline().split())
video = list(map(int,sys.stdin.readline().split()))



def check(video,mid,M):
    count = 1
    sum = 0
    print(f"Checking mid = {mid}")  # 현재 mid 출력
    for i in video:
        print(f"  Current video = {i}, sum = {sum}")  # 각 비디오와 그때의 합 출력
        if sum+i > mid:
            # 다음 숫자로 넘어감, 블루레이 개수 추가
            count += 1
            sum = 0
        sum += i
        print(f"    Updated sum = {sum}, count = {count}")  # 새로 갱신된 sum과 count 출력
    print(f"  Total count = {count}, M = {M}")
    return count <= M

    

def binary_search(video,M):
    left = max(video)
    right = sum(video)
    answer = right
    print(f"Initial left = {left}, right = {right}")  # 초기 left, right 출력
    
    while left <= right:
        mid = (left+right)//2
        print(f"\nBinary search: left = {left}, right = {right}, mid = {mid}")
        
        if check(video,mid,M):
            answer = mid
            right = mid -1
        else:
            left = mid +1
    return answer

print(f"Minimum Blu-ray size: {binary_search(video, M)}")

