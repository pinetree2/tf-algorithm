# 트리의 개수를 세는 프로그램

import sys 



def checkTree(graph,v,visited,parent):
    visited[v] = True #현재 노드 방문 처리 
    for i in graph[v]:# 인접(이웃)노드 탐색
        if not visited[i]: #방문하지 않은 노드라면 방문하되,
            if not checkTree(graph,i,visited,v): 
                return False #탐색 중 사이클이 발견되면 False 반환
        elif i != parent: #방문한 노드인데 부모노드가 아니라면 
            return False
    return True # 모든 노드 탐색 후 사이클이 없으면 True반환
    

testcase =0
while True:
    testcase +=1
    n,m = map(int,sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    graph= [ [] for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(m):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    tree_count =0
    for i in range(1,n+1):
        if not visited[i]:
            if checkTree(graph,i,visited,-1):
                tree_count +=1
    
    if tree_count == 0:
        print(f'Case {testcase}: No trees.')
    elif tree_count == 1:
        print(f'Case {testcase}: There is one tree.')
    else:
        print(f'Case {testcase}: A forest of {tree_count} trees.')

'''
이 코드에서 처음에 내가 고려하지 못한 것
- dfs탐색이 끝나면 또 탐색해야함 ( 테스트케이스 1처럼 트리가 여러개인경우 )
- 그리고, 트리의 개수를 어떻게 세야할지 모르겠음 
- 사이클이 생기는 경우 (어떻게 판단하는지 모름) --> 부모노드로 판단한다. 


'''