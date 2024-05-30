# 5.30
import sys
# 로그에 기록된 출입 기록의 수 n
n = int(sys.stdin.readline().strip())
#dictionary = {}
# n개의 줄에 출입 기록이 순서대로 주어짐, string 으로 주어짐 
now = []
for _ in range(n):
  # string 두개 입력받기
  a, b = sys.stdin.readline().strip().split()
  #dictionary[a] = b
  if b == "enter":
    now.append(a)
  else :
    if a in now:
      now.remove(a)
now = sorted(now,reverse=True) # 문자열 역순 
print(*now,sep='\n') # 줄바꿈, [] 없이, 한줄씩 출력 


---
# 시간초과를 안하는 방법 
import sys

# 로그에 기록된 출입 기록의 수 n
n = int(sys.stdin.readline().strip())
now = set()  # 현재 사무실에 있는 사람을 저장할 집합

for _ in range(n):
  # string 두 개 입력받기, 끝의 개행 문자 제거를 위해 strip 사용
  a, b = sys.stdin.readline().strip().split()
  if b == "enter":
    now.add(a)
  else:  # b == "leave"
    now.discard(a)  # 집합에서 안전하게 제거

# 집합을 리스트로 변환 후 역순으로 정렬
now_sorted = sorted(now, reverse=True)

# 줄바꿈으로 출력
for name in now_sorted:
    sys.stdout.write(name + '\n')


# 시간초과..를 이렇게 해야 안하는디..........