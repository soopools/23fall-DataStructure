class ArrayList: # 1. 클래스 선언

    # 2. 전역변수 > 멤버 변수로 변환
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    def isEmpty(self): 
        return self.size == 0 

    def isFull(self):
        return self.size == self.capacity

    def insert(self, pos, e):
        # global size # 전역 변수
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range (self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1
            return e

        else:
            print("Overflow or Invalid Position")

    def display(self):
        for i in range(self.size):
            print (self.array[i], end = '')
        print()

    # 삭제 연산
    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size: # 0 <= position <=  : 포지션의 경우 사이즈가 5번째 칸으로 되어 있으므로(비어 있는 위치), insert 함수 구성할 때와 마찬 가지로 같거나 크다 하면 안됨
            e = self.array[pos]
            for i in range (pos, self.size-1): # 1안: position+1 부터 size 전까지, 2안: 
                self.array[i] = self.array[i+1] # 오른쪽에서 왼쪽으로 오는 거니까
            self.size -= 1
            return e
        
        else:
            print("Underflow or Invalid Position")

    
    # if __name__ == "__main__":
    #     insert(0, 'A')
    #     insert(0, 'B')
    #     insert(size, 'C')
    #     insert(1, 'D')

    #     display()

    #     delete(2)
    #     display()