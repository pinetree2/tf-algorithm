import sys 
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

def solution(N,P):
    '''
    3
    3+1 = 4
    3+1+4 = 8
    3+1+4+3 = 11
    3+1+4+3+2 = 13

    answer = 3+4+8+11+13
    근데 이게 최솟값인걸 찾아야한다.. 

    1 2 3 3 4 로 오름차순 정렬하면
    1 = 1
    1 2 = 3
    1 2 3 = 6 
    1 2 3 3  = 9
    1 2 3 3 4 = 13
    오호라 그냥 오름차순 해버리는게 속편하군
    이거근데 일종의 피보나치 느낌 같은데
    어.. 너무 옛날에 해서 구현방법 기억안남 

    '''

    P.sort()
    answer = 0
    for i in range(N):
        answer += sum(P[:i+1])
    return answer

print(solution(N,P))
