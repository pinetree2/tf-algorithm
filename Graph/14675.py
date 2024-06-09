import sys

N = int(sys.stdin.readline())
# 트리 입력받는다.
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
  u, v = map(int,sys.stdin.readline().split())
  tree[u].append(v)
  tree[v].append(u)

q = int(input())
cnt = 0
for _ in range(q):
  t,k = map(int,input().split())
  if t == 1 :
    # k 번째 정점이 단절점인지
    if len(tree[k]) < 2:
      print("no")
    else:
      print("yes")
    
  elif t == 2 :
    # k 번째 간선이 단절선인지 
    print("yes")


