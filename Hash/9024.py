from itertools import combinations


def solve(arr,k):
  combine = list(combinations(arr,2))
  print("조합결과")
  print(combine)
  before = 0
  answer = 1

  for i in combine:
    if i[0]+i[1]-k < before:
      answer = 1
      before = i[0]+i[1]-k
    
    elif (i[0]+i[1]-k) == before:
      answer +=1

    elif (i[0]+i[1]-k) ==0:
      answer +=1
      before = 0

  
  return answer 
    

k = int(input())
for _ in range(k):
  n,k= map(int, input().split())
  # 크기 n 만큼의 배열 입력받기
  arr = list(map(int, input().split()))
  if len(arr) == n :
    print(solve(arr,k))

