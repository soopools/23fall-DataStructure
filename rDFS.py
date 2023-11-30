# 깊이 우선 탐색 (Depth First Search)

Vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
AdjVer = [[1, 2], 
          [0, 3],
          [0, 3, 4],
          [1, 2, 5],
          [2, 6, 7],
          [3],
          [4, 7],
          [4, 6]]

visited = [False] * len(Vertex)

def rDFS(u): # 정점 번호가 날아오면
    visited[u] = True # 방문 기록 남기기
    print(Vertex[u], end=' ')

    for v in AdjVer[u]:
        if visited[v] == False: # if not visited[v]:
            rDFS(v) # 재귀 호출로 방문

if __name__ == '__main__':
    print('rDFS: ', end='')
    rDFS(0)