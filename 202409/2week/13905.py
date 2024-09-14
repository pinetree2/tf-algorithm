from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

def find_parent(n,parent): # 부모 노드 찾기
    if parent[n] !=n:
        parent[n] = find_parent(parent[n],parent)
    return parent[n]


def union(a,b,parent):
    a = find_parent(a,parent)
    b = find_parent(b,parent)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 가중치가 큰 순서대로 정렬 
# s에서 시작해서 e까지 가는 경로 중 가장 큰 가중치를 찾는다.

N,M = map(int,stdin.readline().split())
s,e = map(int,stdin.readline().split())
edges = []
for _ in range(M):
    a,b,c = map(int,stdin.readline().split())
    edges.append((c,a,b))


#부모 배열 초기화
parent = [i for i in range(N+1)]

# 내림차순으로 edges 정렬
edges.sort(reverse=True)

# 근데 여기서 조건이 붙는다. s 에서 시작해서 e까지 가는 경로 중 가장 큰 가중치를 찾아야 한다.
# 특정 정점에서 탐색을 시작해서 특정 정점에 도달하면 끝내야 한다.
# s에서 e까지 가는 경로를 찾기 위해 union-find를 사용하여 경로를 연결한다.
# N-1개의 간선을 선택하여 최대 신장 트리를 만든다.
    
answer = 0


for c,a,b in edges:
    # 부모노드가 같으면 사이클이 생기기 때문에, 같지 않아야 한다. 
    if find_parent(a,parent) != find_parent(b,parent):
        union(a,b,parent)
        # s와 e가 같은 집합에 속하게 되면, s에서 e까지의 경로가 연결된 것이다. 두 노드가 연결되는 순간 종료!
        if find_parent(s, parent) == find_parent(e, parent):
            answer = c
            break


print(answer)