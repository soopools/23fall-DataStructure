from ArrayStack import ArrayStack

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1']
]

SIZE = 6

def isValidPos(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE: # 맵의 범위를 벗어나지 않았는데,
        if map[r][c] == '0' or map[r][c] == 'x': # 값이 0이거나 exit이면
            return True # 갈 수 있음 (valid position)
        
    return False # 아니면 갈 수 없음 (invalid position)
    
def DFS():
    print("DFS: ")
    S = ArrayStack(100)
    S.push((1, 0)) # 시작 위치: 1행 0열

    while not S.isEmpty(): # 스택이 비어 있지 않으면 > 방문할 위치가 있음을 의미
        pos = S.pop() # 스택에서 위치를 꺼내서
        print(pos, end = '->') # 방문한 위치를 출력하고
        (r, c) = pos # 행과 열로 분리

        if (map[r][c] == 'x'):
            return True # 출구에 도착한 경우
        else:
            map[r][c] = '.' # 한 번 방문했다는 의미로 0/1이 아닌 .을 표기

            if isValidPos(r-1, c): S.push((r-1, c)) # 상하좌우 이동할 곳 있는지 확인
            if isValidPos(r+1, c): S.push((r+1, c)) # 상하좌우 이동할 곳 있는지 확인
            if isValidPos(r, c-1): S.push((r, c-1)) # 상하좌우 이동할 곳 있는지 확인
            if isValidPos(r, c+1): S.push((r, c+1)) # 상하좌우 이동할 곳 있는지 확인
        
        S.display()

    return False # 출구에 도착하지 못한 경우

# Test code
result = DFS()
if result:
    print(" --> 미로 탐색 성공")
else:
    print(" --> 미로 탐색 실패")