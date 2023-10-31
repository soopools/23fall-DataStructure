class CircularQueue:
    def __init__(self, capacity = 8): # 원형 큐의 경우, 7에서 0으로 넘어가는 거 보려면 너무 요소들이 많이 필요해서 일단 작게 잡아 놓음
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.front = self.rear = 0 # front와 rear를 0으로 초기화

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity # 조정
            self.queue[self.rear] = e
        else:
            print("Queue is full !")

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.queue[self.front]
        else:
            print("Queue is empty !")
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[(self.front + 1) % self.capacity]
        else:
            print("Queue is empty !")
    
    # 큐에서는 디스플레이 구현이 제일 까다로움
    def display(self):
        print('front: %d - rear: %d' % (self.front, self.rear), end = ' ') # 출력은 front 다음부터 어저구..

        # do while 문처럼 만든 어쩌구 / 근데 이거 말고 do-while문 써도 됨
        i = self.front

        while i != self.rear:
            i = (i + 1) % self.capacity # 인덱스 움직이고
            print('[%c] ' % self.queue[i], end = '-> ') # 출력하고

        print('\b\b\b   ')

    # 반복문 중요    ,, 

if __name__ == '__main__':
    Q = CircularQueue(5)

    Q.enqueue('A'); Q.display()
    Q.enqueue('B'); Q.display()
    Q.enqueue('D'); Q.display()
    Q.enqueue('C'); Q.display()
    
    print('Dequeqe --> ', Q.dequeue()); Q.display()
    print('Dequeqe --> ', Q.dequeue()); Q.display()