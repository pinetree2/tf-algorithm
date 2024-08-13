S = input()
zero_num = S.count('0')//2
one_num = S.count('1')//2
answer = ""
def check_S(S):
  for i in range(len(S)):
    if (i%2 == 0 and S[i] != '1') or (i%2 ==1 and S[i] !='0'):
      return False
  return True

# 서브태스크 1 충족 
if len(S)%4 == 0 :
  #S의 홀수번째 문자가 1, 짝수번째 문자가 0을 충족하는지 확인하기
  if check_S(S):
  
    # 개수를 기반으로 문자열 만들기 
    for _ in range(zero_num):
      answer+='0'
    for _ in range(one_num):
      answer+='1'
      
# 서브태스크 2
else:
  #S 문자열 인자 개수 셈
  # 개수를 기반으로 문자열 만들기 
  for _ in range(zero_num):
    answer+='0'
  for _ in range(one_num):
    answer+='1'
  

# answer 출력
print(answer)
  