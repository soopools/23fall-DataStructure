'''
DFS-iterative(G, v):

스택 S를 생성한다.
S.push(v)

while(not is_Empty(S)) do
    v = S.pop()                 # pop 하는 건 DFS 아니고 BFS 방식
    if (v is not visited)
        v를 방문되었다고 표시
        for all u ∈ (v에 인접한 정점) do
            S.push(u)를 한다.
        
'''

# 깊이 우선 탐색

def DFS_iterative(G, v):
    stack = []
    stack.append(v)
    visited = []

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for u in G[v]:
                stack.append(u)
    return visited

