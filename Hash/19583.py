import sys 
input = sys.stdin.readline
# S,E,Q는 22:00 와 같이 시간형식의 string 이다.
S,E,Q = map(str, input().split())
S = int(S[:2]+S[3:])
E = int(E[:2]+E[3:])
Q = int(Q[:2]+Q[3:])


attend = set()
answer =0 
while True:
  try:
    time,name = input().split()
    time = int(time[:2]+time[3:])
    if time <= S:
      attend.add(name)
    elif E <= time <= Q and name in attend:
      attend.remove(name)
      answer +=1
  except:
    break

print(answer)


## 시간 초과 이슈는 항상 hash 기반의 dict 쓰거나, sys input 안스는경우,,,
