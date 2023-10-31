class Node: 
    def __init__(self, data, next):
        self.data = data # reset
        self.next = next #

# 원형 연결 리스트의 경우 중요도: 포지션 찾기 < 앞 뒤에 일어나는 일들
class QueueType:
    def __init__(self):
        self.tail = None # 스택 초기화 (= None)
        self.size = 0    # 노드의 개수

    def isEmpty(self):  # def isFull: 은 의미가 없음
        return self.tail == None

    # 원형 연결 리스트를 통해 큐를 규현하기 > 
    def enqueue(self, data): # insertLast() 가 조금 더 적합한 이름이엇다  ,, , ? 
        node = Node(data, None) # 보류 시키기

        # 노드 삽입 시 경우의 수 2개 생각
        # 1. 리스트가 비어 있는 경우
        if self.isEmpty():
            self.tail = node # 날 누가 가리키지 ?!? > tail이
            node.next = node # 난 누굴 가리키지 ?!? > 자신을 가리키게 하기

        # 2. 리스트가 비어 있지 않은 경우
        else: 
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
        
        self.size += 1

    def insertFirst(self, data): # insertLast() 가 조금 더 적합한 이름이엇다  ,, , ? 
        node = Node(data, None) # 보류 시키기

        # 노드 삽입 시 경우의 수 2개 생각
        # 1. 리스트가 비어 있는 경우
        if self.isEmpty():
            self.tail = node # 날 누가 가리키지 ?!? > tail이
            node.next = node # 난 누굴 가리키지 ?!? > 자신을 가리키게 하기

        # 2. 리스트가 비어 있지 않은 경우
        else: 
            node.next = self.tail.next
            self.tail.next = node
            # self.tail = node # 나는 첫 번째 노드니까 이 줄을 없애주면 됨
        
        self.size += 1

    def dequeue(self): #deleteFirst()
        if not self.isEmpty(): # 삭제할 노드가 하나라도 있다면
            p = self.tail # 삭제할 노드의 이전 노드를 찾기 위해
            q = p.next # 삭제할 노드
            data = q.data # 삭제할 노드의 데이터를 저장

            if p == q:
                self.tail = None # 삭제할 노드가 마지막 노드라면
                
            else: 
                p.next = q.next

            self.size -= 1 # 노드 개수 감소에 따른 사이즈 감소
            # 사이즈 변화 안 주면 self.tail이 삭제된 노드의 주소를 그대로 갖고 있음, 꼭 삭제해 줘야 함 !!
            return data
        
    def deleteLast(self):
        '''
        ~~ 시험 공부 한다 생각하고 직접 해보기 ~~
        '''
            
    def display(self):
        if not self.isEmpty():
            p = self.tail.next
            
            for i in range(self.size):
                print('[%s] -> ' % p.data, end = '')
                p = p.next
        print('\b\b\b    ')
        
if __name__ == '__main__':
    Q = QueueType()
    
    Q.enqueue('Apple'); Q.enqueue('Carrot'); Q.display()
    Q.insertFirst('Durian'); Q.insertFirst('Eggplant'); Q.display()

    print ('[%s] is deleted.' %Q.dequeue()); Q.display()

# 연결된 표현볍은 그냥 플밍 구현 방법
