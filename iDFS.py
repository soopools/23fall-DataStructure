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

from queue import LifoQueue

def iDFS(u):
    S = LifoQueue() # 스택 생성
    S.put(u)     # push(u)

    while not S.empty():
        u = S.get() # 3을 빼서 u에 넣음
        S.put(u)    # push(u) : 3을 다시 넣음
        ## 위에 두 줄은 peek()와 같은 역할을 함

        if visited[u] == False:
            visited[u] = True
            print(Vertex[u], end=' ') # 캐릭터로 출력

        flag = True # false 도 가능

        for v in AdjVer[u]: # 인접 정점 중 순차적으로 방문
            if visited[v] == False:
                S.put(v)
                flag = False # 반복문에 들어온 경우에는 flag를 false로 바꿔줌
                break
            # 인접 정점 방문 이후 바로 빠져 나와야 DFS (방문하지 않은 애들 스택에 넣는 것 아님)

        if flag == True:
            S.get()
            
        S.get()



if __name__ == '__main__':
    print('iDFS(A): ', end='')
    iDFS(0)
