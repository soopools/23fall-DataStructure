# 너비 우선 탐색 (Breadth First Search)

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

from queue import Queue # built-in module

def BFS(u):
    Q = Queue() # 큐 생성

    Q.put(u) # 시작 정점을 큐에 삽입

    visited[u] = True         # 방문 기록 남기기
    print(Vertex[u], end=' ') # 정점 번호에 해당하는 데이터 출력
    
    while not Q.empty():          # 큐가 비어있지 않으면
        u = Q.get()               # 큐에서 정점 번호를 꺼내
        
        for v in AdjVer[u]:         # 인접 정점들 중에서
            if visited[v] == False: # 방문하지 않은 정점이 있으면
                Q.put(v)            # 큐에 삽입
                visited[v] = True   # 방문 기록 남기기
                print(Vertex[v], end=' ')

if __name__ == '__main__':
    print('BFS(E): ', end='')
    BFS(4) # alphabet E