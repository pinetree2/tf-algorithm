# 배열과 M이 주어졌을 때, 구간(구간에 속한 수의 최댓값 - 최솟값)의 점수의 최댓값의 최솟값을 구하는 프로그램

'''
1. 구간을 나눈다. (어떻게..)
2. 나눈 구간별로 최댓값과 최솟값의 차를 구한다. 
3. 구간별로 나온 값들을 정렬한다.
4. 정렬된 값들 중에서 가장 큰 값을 저장해놓는다.
5. 또 다른 구간을 나눠본다.
6. 2~5번을 반복한다.
7. 저장된 값 중에서 가장 작은 값을 출력한다.
여기에서 어떻게 parametric search를 적용해야할지 모르겠다.
아 ㄹ ㅇ 감도안잡힘 

중간값을 무엇으로 해야하는지 모르겠으며, 무엇의 최대최소를 가깝게 해야하는가.. 
구간은 어떻게 나눠야 하는가..

---

- 구간을 나눌 기준 값을 변경해가면서 나눌 구간을 찾는다. 
- 기준 값을 증가 or 감소시키면서 구간을 만들어주는데, 이 기준 값을 이분 탐색으로 구한다.

이해가 안되었던 점

-> 왜 mid를 이용해서 구간을 나누는지


'''

# 지피티가 짜준 코드....
import sys
# 입력 처리


def check(arr, mid, M):
    count = 1  # 최소 1개의 구간 필요
    min_val, max_val = arr[0], arr[0]

    for num in arr[1:]:
        min_val = min(min_val, num)
        max_val = max(max_val, num)

        if max_val - min_val > mid:
            count += 1  # 새 구간 시작
            min_val, max_val = num, num  # 새 구간 초기화

    return count <= M  # M개 이하로 나눌 수 있으면 True

def binary_search(M, arr):
    
    left, right = 0, max(arr) - min(arr)
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if check(arr, mid, M):  # mid로 M개 이하 구간 만들 수 있음
            answer = mid
            right = mid - 1  # 더 작은 값 탐색
        else:
            left = mid + 1  # 더 큰 값 탐색

    return answer


N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

# 결과 출력
print(binary_search(M,arr))

# 다시 제대로 이해하고 풀자...