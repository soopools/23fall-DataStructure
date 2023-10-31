# 10/12/23 Week6 (2)
from CircularQueue import CircularQueue

class CircularDeque(CircularQueue): # CircularDeque inherits from CircularQueue (멤버 method 전부 사용할 수 있게끔 상속)
    # 두 개 클레스가 부모 자식 관계에 있으면, deque(부모)가 먼저 만들어 져야 함
    def __init__(self, capacity = 10):
        super().__init__(capacity)

    # isEmpty(), isFull(), display()는 CircularQueue에서 상속 받음
    
    def addFront(self, e):
        # 프론트는 항상 비어 있는 공간을 가지므로, 프론트에 데이터를 삽입하면 프론트는 한 칸 앞으로 이동
        if not self.isFull():
            self.queue[self.front] = e
            self.front = (self.front - 1 + self.capacity) % self.capacity # self.capacity = N을 의미
        else: pass # 생략한다는 의미, or "print("Queue is full !")"

    def addRear(self, e):
        self.enqueue(e) # 부모 클래스의 enqueue() 메소드 호출

    def deleteFront(self):
        self.dequeue() # 부모 클래스의 dequeue() 메소드 호출

    def deleteRear(self):
        if not self.isEmpty():
            e = self.queue[self.rear] # rear가 가리키는 값을 가져오고
            self.rear = (self.rear - 1 + self.capacity) % self.capacity # 가리키는 애를 지우고, rear를 반시계 방향으로 이동
        else: pass # 생략

    def getFront(self):
        self.peek() # 부모 클래스의 peek() 메소드 호출

    def getRear(self):
        if not self.isEmpty():
            return self.queue[self.rear]
        else: pass

if __name__ == '__main__':

    import random # 모듈 가져오기

    D = CircularDeque()
    
    for i in range(4):
        D.addFront(random.randint(65, 90))
    D.display() # circularQueue에 정의된 display() 메소드 호출
 
    for i in range(3):
        D.addFront(random.randint(65, 90))
    D.display() # circularQueue에 정의된 display() 메소드 호출
 
    for i in range(2):
        D.deleteFront()
    D.display() # circularQueue에 정의된 display() 메소드 호출
     
    for i in range(2):
        D.deleteRear()
    D.display() # circularQueue에 정의된 display() 메소드 호출