# 5.30
# N 과 M 을 입력받는다 int로
N,M = map(int, input().split())

# N개의 줄에 걸쳐 key : 주소, 비밀번호 : 알파벳 대문자 
# N개 입력 끝나면 M개의 줄에 걸쳐 찾으려는 사이트 주소 입력받음 

dict = {}
find_site = []
answer = []
for _ in range(N):
  site,pw = input().split()
  dict[site]= pw

for _ in range(M):
  find = input()
  if find in dict:
    answer.append(dict[find])


print(*answer,sep='\n')

