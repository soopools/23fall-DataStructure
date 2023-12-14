def find_min_max(A):
    min = A[0]
    max = A[0]
    
    for i in range(1, len(A)):
        if min > A[i]: min = A[i] 
        if max < A[i]: max = A[i]

    return (min, max)

if __name__ == '__main__': # 해당 파일 안에서만 if문 안 명령들 실행, 외부 참조 시 해당 구문은 실행되지 않음.
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    (x, y) = find_min_max(data)
    print ("min, max =", (x, y))