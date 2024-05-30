# 5.30
# n = int(input())
# cnt = 0
# arr = list(map(int,input().split()))
# if len(arr) == n:
#   x = int(input())
#   for i in arr:
#     if x-i in arr:
#       cnt +=1

# print(int(cnt/2))

# 놀랍지 않게도 시간초과 ㅎㅎ 
# 해시를 기반으로 하는 set 을 써야한다.
n = int(input())
cnt = 0
arr = list(map(int,input().split()))
arr_set = set(arr)

x = int(input())
if len(arr) == n:
  for i in arr:
    if x-i in arr_set:
      cnt +=1

print(int(cnt/2))