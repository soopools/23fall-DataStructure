data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
# 트리로 힙 만들 땐 0번 인덱스 안 썼으나, 
def heapSort():
    n = len(data)

    for i in range(n // 2-1, -1, -1): # 0까지 1씩 감소
        heapify(i, n)
        print('i = ', i, data)
    print()

    for i in range(n-1, 0, -1): # 왜 이렇게 돌아가는지 손으로 한 번 따라가보기
        data[i], data[0] = data[0], data[i]
        heapify(0, i)
        print('i =', i, data)

def heapify(i, n):
    largest = i
    l = 2*i +1
    r = 2*i +2

    if l < n and data[i] < data[l]:
        largest = l
    
    if r < n and data[largest] < data[r]:
        largest = r

    if largest != i: # largest == i , i가 제일 큰 값이라 바꿔 줄 필요 없음
        data[i], data[largest] = data[largest], data[i]
        heapify(largest, n)

if __name__ == '__main__':
    print("Origin: ", data)
    heapSort()
