from ArrayList import ArrayList

capacity = 100
array = [None] * capacity
size = 0

def isEmpty():
    return size == 0

def isFull():
    return size == capacity

def insert(pos, e):
    global size # 전역 변수
    if not isFull() and 0 <= pos <= size:
        for i in range (size, pos, -1):
            array[i] = array[i-1]
            array[pos] = e
            size += 1
    else:
        print("Overflow or Invalid Position")

def display():
    for i in range(size):
        print (array[i], end = '')
    print()

# 삭제 연산
def delete(pos):
    global size

    if not isEmpty() and 0 <= pos < size: # 0 <= position <=  : 포지션의 경우 사이즈가 5번째 칸으로 되어 있으므로(비어 있는 위치), insert 함수 구성할 때와 마찬 가지로 같거나 크다 하면 안됨
        e = array[pos]
        for i in range (pos, size-1): # 1안: position+1 부터 size 전까지, 2안: 
            array[i] = array[i+1] # 오른쪽에서 왼쪽으로 오는 거니까
            size -= 1
        return e
    
    else:
        print("Underflow or Invalid Position")

if __name__ == "__main__":
    L1 = ArrayList(10)
    L2 = ArrayList(7)

    L1.insert(0, 10)
    L1.insert(0, 20)
    L1.insert(L1.size, 30)
    L1.insert(1, 40)
    L1.display()
    
    L2.insert(0, 'B')
    L2.insert(0, 'A')
    L2.insert(1, 'C')
    L2.display()