# 순차 탐색
def seqSearch(A, key):
    n = len(A)
    for i in range(n):
        print(A[i], end=' ') # 어떤 값에 접근했는지 출력
        if A[i] == key:      # 출력한 값이 내가 찾는 값인지 확인
            return i
    return -1                # 찾지 못했을 경우 -1 반환

def rBinSearch(A, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    print(A[mid], end=' ')

    if key == A[mid]:
        return mid
    
    elif key < A[mid]:
        return rBinSearch(A, key, low, mid-1)
    
    else: # key > A[mid]
        return rBinSearch(A, key, mid+1, high)
    
# def iBinSearch(A, key):
    # low = 0; high = len(A) - 1
def iBinSearch(A, key, low, high):

    while(low <= high):
        mid = (low + high) // 2
        print(A[mid], end=' ')

        if key == A[mid]:
            return mid
        
        elif key < A[mid]:
            high = mid - 1
        
        else:
            low = mid + 1

    return -1

def interpolationSearch(A, key, low, high):
    if (low > high):
        return -1

    mid = int(low + (high - low) * (key - A[low]) / (A[high] - A[low]))
    print(A[mid], end=' ')

    if key == A[mid]:
        return mid
    
    elif key < A[mid]:
        return interpolationSearch(A, key, low, mid-1)
    
    else: # key > A[mid]
        return interpolationSearch(A, key, mid+1, high)

# test code
if __name__ == '__main__':
    import random
    from Sorting import selectionSort

    A = []
    for i in range(15):
        A.append(random.randint(1, 100)) # 난수 만들기 ~

    print('A[] = ', A)

    key = int(input('Input to search Key: ')); print()

    print('seqSearch: %d' % seqSearch(A, key)) # 인덱스 seqSearch 호출
    print('rBinSearch: %d' % rBinSearch(A, key, 0, 14)) # 인덱스 rBinSearch 호출
    print('iBinSearch: %d' % iBinSearch(A, key, 0, 14)) # 인덱스 seqSearch 호출