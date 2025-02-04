
'''
이번에는 중복 가능이다. 
'''

import sys
n,m = map(int,sys.stdin.readline().split())
s = []
visited = [False] * (1001)

def dfs():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
            s.append(i)
            dfs()
            s.pop()


dfs()