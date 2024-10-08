import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
# 이.. 숫자의 크기가 꽤나 크다는게 좀 걸리는데,,


# 0에 가장 가까운 용액을 만들어내는 세 용액의 특성값은?
# 그 경우가 2가지 이상인 경우에는 그중에 아무거나 하나만 출력

# arr 에 4개정도 있다 쳐
# arr[0] + arr[1] + arr[2]
# arr[0] + arr[1] + arr[3]
# arr[0] + arr[1] + arr[4]
# arr[0] + arr[2] + arr[3]
# arr[0] + arr[2] + arr[4]
# arr[0] + arr[3] + arr[4]

# arr[1] + arr[2] + arr[3]
# arr[1] + arr[2] + arr[4]
# arr[1] + arr[3] + arr[4]
#...대충 이런느낌인데,, 이걸 머라그러지? 경우의 수 작렬인데
# dfs?!?!?! 투포인터?!?! 근데 할줄을 모름 미치겠음 이게 먼지 알면머함 
# 포인터 1 고정 -> 다른 인덱스 탐색 이런느낌 

arr.sort()
ans = [0,0,0]
res = float('inf') # 초기 결과값을 무한대로 설정  - 최솟값을 찾기 위해

for i in range(N-2):
    left = i + 1
    right = N - 1 # 배열의 맨 끝부터 시작 

    while left < right :
        current_sum = arr[i] + arr[left] + arr[right]

        if abs(current_sum) < abs(res):
            res = current_sum
            ans = [arr[i], arr[left], arr[right]]
        
        if current_sum > 0: # 현재 합이 0보다 크다면, 더 작은 값으로 이동해야함, 배열은 오름차순으로 되어있다.
            right -= 1
        elif current_sum < 0:
            left += 1
        else:
            print(arr[i], arr[left], arr[right])
            break
        
print(ans[0], ans[1], ans[2])


