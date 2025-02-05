# 적어도 M미터의 나무(M넘어도 됨)를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값?
import sys
N,M = map(int,sys.stdin.readline().split()) 
trees = list(map(int,sys.stdin.readline().split()))

def solution():
    start = 1
    end = max(trees)
    
    
    while start <=end:
        mid = (start+end)//2
        length = 0
        for i in trees:
            if i > mid: # 나무의 높이가 절단기의 높이보다 크다면 자른 나머지를 더한다.
                length += i-mid # 자른 길이 
        
        if length >= M: # 자른 길이가 M보다 크거나 같다면, 
            # 더 짧게 남길 수 있는지 
            start = mid + 1 #(절단기 높이 높임)
        else: # 자른 길이가 m보다 작은 길이면, 
            end = mid -1 # 더 길게 남길 수 있는지 확인하기 (절단기 높이 낮춤)

    print(end)

solution()

# 아.. 헷갈리고 어려워......
