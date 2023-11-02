# 정렬된 배열 집합 클래스 

class SortedArraySet:

    def __init__(self, capacity = 100): # 생성자에서는 캐파만 지정
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def contains(self, e): # element가 array 안에 있는지 확인

        for i in range(self.size):
            if self.array[i] == e: # i번째 인덱스가 e와 같으면
                return True
            
            return False # 반복문 다 돌렸는데도 같은 것이 없다면 False
        
    def insert(self, e): # element를 array에 넣는다.
        if self.contains(e) or self.isFull():
            return False # insert 불가하므로 종료
        
        self.array[self.size] = e; # 현재 배열에 비어 있는 첫 번째 공간에 element 삽입
        self.size += 1 # size 1 증가

        # 정렬 시작
        for i in range(self.size - 1, 0, -1): # 방금 전에 들어간 element의 인덱스를 역으로 움직이면서 
            if self.array[i-1] <= self.array[i]:
                break
            self.array[i-1], self.array[i] = self.array[i], self.array[i-1] # element를 삽입한 후에는 정렬된 상태를 유지해야 하므로, element를 삽입한 인덱스부터 시작해서 왼쪽으로 이동하면서 정렬된 상태를 유지
        # 정렬 완료

    def union(self, setB): # 합집합
        setC = SortedArraySet

        i = 0; j = 0;

        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]

            if a == b:
                setC.append(a)
                i += 1; j += 1
            elif a < b:
                setC.append(a)
                i += 1
            else:
                setC.append(b)
                j += 1

        while i < self.size:
            setC.append(self.array[i])
            i += 1

        while j < setB.size:    
            setC.append(setB.array[j])
            j += 1
        
        return setC

    def intersect(self, setB): # 교집합
        setC = SortedArraySet

        i = 0; j = 0;

        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]

            if a == b:
                setC.append(a)
                i += 1; j += 1
            elif a < b:
                setC.append(a)
                i += 1
            else:
                j += 1

        return setC

    def difference(self, setB): # 차집합
        setC = SortedArraySet

        i = 0; j = 0;

        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]

            if a == b:
                setC.append(a)
                i += 1; j += 1
            elif a < b:
                setC.append(a)
                i += 1
            else:
                j += 1

        while i < self.size:
            setC.append(self.array[i])
            i += 1
        
        return setC
    
    def __str__(self):
        return str(self.array[0:self.size]) # 배열의 처음부터 size까지만 출력
    
if __name__ == '__main__':
    import random
    
    setA = SortedArraySet()
    setB = SortedArraySet()

    for i in range(5):
        setA.insert(random.randint(1, 9))
        setB.insert(random.randint(1, 9))

    print('Set A =', setA)
    print('Set B =', setB)

    e = int(input('Input to delete: '))
    setB.delete(e)
    print('Set B:'  , setB)

    print (setA == setB)

    print('A U B : ', setA.union(setB))
    print('A ^ B : ', setA.intersect(setB))
    print('A - B : ', setA.difference(setB))
