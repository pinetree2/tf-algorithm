import sys

def prefix_length(s1, s2):
    """s1과 s2의 앞부분에서 일치하는 길이를 계산"""
    length = min(len(s1), len(s2))  # 두 문자열 중 짧은 쪽에 맞춰 비교
    for i in range(length):
        if s1[i] != s2[i]:
            return i  # 일치하지 않으면 그 위치까지의 길이 반환
    return length  # 전체가 일치할 경우

N = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for _ in range(N)]

max_len = 0
answer = (0, 1)  # 가장 많이 일치하는 두 문자열의 인덱스 저장

# 모든 쌍의 문자열 비교
for i in range(N):
    for j in range(i + 1, N):
        common_len = prefix_length(arr[i], arr[j])  # 두 문자열의 일치 길이
        if common_len > max_len:
            max_len = common_len
            answer = (i, j)  # 일치하는 길이가 더 크면 결과 갱신

# 결과 출력
print(arr[answer[0]])
print(arr[answer[1]])
