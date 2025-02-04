'''
백트래킹 : 불필요한 경로를 조기에 차단한다. 답이 될 만한지 판단하고 그렇지 않으면 그 부분까지 탐색하는 것을 하지 않고 가지치기 하는 것

'''
import sys 
n,m = map(int,sys.stdin.readline().split())

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return

    for i in range(1,n+1):
        if i not in s:
           s.append(i)
           dfs() #재귀 
           '''
           ex ) 
           n = 4, m =2
           1 삽입 후 [1,2] -> 2 pop ->[1,3] -> 3 pop -> [1,4] -> 4 pop 
           재귀가 끝나고 1도 pop
           '''
           s.pop()

dfs()