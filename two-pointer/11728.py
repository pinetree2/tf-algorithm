import sys 

N,M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

# 두 배열이 정렬되어있기 때문에, 두개의 포인터를 사용해서 비교하며 새로운 배열을 만든다. 
i,j =0,0
result = []

while i<N and j<M:
    if A[i] < B[j]:
        result.append(A[i])
        i+=1
    else:
        result.append(B[j])
        j+=1

result.extend(A[i:])
result.extend(B[j:])

print(*result) # 리스트를 언패킹(*result)하여 공백으로 구분된 문자열로 출력

'''

두 배열을 한 번씩만 순회 → 
𝑂(𝑁+𝑀)
O(N+M)
정렬된 두 배열을 효율적으로 합치는 "Merge Sort의 병합 과정" 과 같은 방식
'''