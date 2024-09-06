import sys
N = int(sys.stdin.readline())
# N개의 길이를 가진 배열에 key:value로 값 넣기

arr= list(map(int,sys.stdin.readline().split()))
i = 0
time =0
answer = [0]*N
#enumrate 가 리스의 모든 인덱스를 차례대로 순회하기 때문에 인덱스 증감을 수동으로 처리하지 않아도 된다.
while any(value > 0 for value in arr):
  for idx, value in enumerate(arr): 
    if value > 0 :
      arr[idx] -=1
      time +=1
      if value ==1:
        answer[idx] = time

    elif value == 0:
      continue 

print(*answer)