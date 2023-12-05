Graph = {'A':[('B', 10), ('F', 3), ('G', 7)],
         'B':[('A', 10), ('D', 9), ('G', 6)],
         'C':[('D', 2), ('G', 4)],
         'D':[('B', 9), ('C', 2), ('E', 4), ('F', 11), ('G', 10)],
         'E':[('D', 4), ('F', 5)],
         'F':[('A', 3), ('D', 11), ('E', 5), ('G', 2)],
         'G':[('A', 7), ('B', 6), ('C', 4), ('D', 10), ('F', 2)]}

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

def dijkstra(vName): # (시작 정점)
    vCnt = len(Graph)
    dist[(ord(vName) - 65)] = 0 # reset

    for i in range(vCnt):
        vNum = findMin()
        vName = chr(vNum + 65)

        visited[vNum] = True
        print('[%c(%d)] ' % (vName, dist[vNum]), end='')

        for e in Graph[vName]:
            vNum2 = ord(e[0]) - 65
            if visited[vNum2] == False:
                if dist[vNum] + e[1] < dist[vNum2]:
                    dist[vNum2] = dist[vNum] + e[1]

if __name__ == '__main__':
    dijkstra('A')