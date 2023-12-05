Graph = {'A':[('B', 29), ('F', 10)],
         'B':[('A', 29), ('C', 16), ('G', 15)],
         'C':[('B', 16), ('D', 12)],
         'D':[('C', 12), ('E', 22), ('G', 18)],
         'E':[('D', 22), ('F', 27), ('G', 25)],
         'F':[('A', 10), ('E', 27)],
         'G':[('B', 15), ('D', 18), ('E', 25)]}

INF = 100
dist = [INF] * len(Graph) # 시작 정점에서 각 정점까지의 거리
visited = [False] * len(Graph) # 방문한 정점을 표시

def findMin(): # 최솟값 찾기
    minDist = INF
    minV = 0 # minVertex

    for v in range(len(dist)):
        if visited[v] == False and dist[v] < minDist:
            minDist = dist[v]
            minV = v
    return minV

# case I # print()를 for문 밖에 넣어서 출력
# def prim(vName):
#     vCnt = len(Graph)
#     dist[(ord(vName) - 65)] = 0 # 시작 정점의 거리를 0으로 설정: 초기화

#     for i in range(vCnt):

#         vNum = findMin()
#         vName = chr(vNum + 65)

#         visited[vNum] = True
#         print('[%c(%d)] ' % (vName, dist[vNum]), end='')

#         # dynamic programming
#         for e in Graph[vName]: # vName에 인접한 정점들
#             vNum - ord(e[0]) - 65
#             if (visited[vNum] == False and e[1] < dist[vNum]):
#                 dist[vNum] = e[1]

# case II # print()를 for문 안에 넣어서 출력
def prim(vName):
    vCnt = len(Graph)
    dist[(ord(vName) - 65)] = 0 # 시작 정점의 거리를 0으로 설정: 초기화

    for i in range(vCnt):
        for j in range(vCnt):
            print('%3d ' % dist[j], end='')
        print()

        vNum = findMin()
        vName = chr(vNum + 65)

        visited[vNum] = True
        # print('[%c(%d)] ' % (vName, dist[vNum]), end='')

        # dynamic programming
        for e in Graph[vName]: # vName에 인접한 정점들
            vNum - ord(e[0]) - 65
            if (visited[vNum] == False and e[1] < dist[vNum]):
                dist[vNum] = e[1]

if __name__ == '__main__':
    prim('C') # 시작 정점 다른 걸로 해도 결과는 동일