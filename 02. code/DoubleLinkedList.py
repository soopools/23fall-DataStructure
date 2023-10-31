class Node: 
    def __init__(self, data, prev, next):
        self.data = data # reset
        self.prev = prev
        self.next = next #

class DoubleLinkedType:
    def __init__(self):
        self.front = self.rear = None # 덱 만들어서 front-rear 이용, None으로 초기화
        self.size = 0    # 노드의 개수

    def isEmpty(self):  # def isFull: 은 의미가 없음
        return self.size == 0

    def addFront(self, data):
        node = Node(data, None, self.front) # 내 왼쪽은 none, 오른쪽은 현재 리스트의 첫 번째

        # 날 가리킬 때, (내가 빈 방에 들어 왔을 때), 다른 노드는 날 가리키지 못함
        if self.isEmpty():
            # 유일한 노드인 나 > 내가 프론트 겸 리어 (빈방이라 노드가 날 가리키지는 않음)
            self.front = self.rear = node

        else: # 누가 나를 가리킬지
            self.front.prev = node
            self.front = node # 노드를 먼저 가리키면 주소 날아감 / 윗줄 아랫줄 순서 바뀌면

        self.size += 1

    def addRear(self, data):
        node = Node(data, self.rear , None) # 내 왼쪽은 none, 오른쪽은 현재 리스트의 첫 번째
        
        # 날 가리킬 때, (내가 빈 방에 들어 왔을 때), 다른 노드는 날 가리키지 못함
        if self.isEmpty():
            # 유일한 노드인 나 > 내가 프론트 겸 리어 (빈방이라 노드가 날 가리키지는 않음)
            self.front = self.rear = node

        else: # 누가 나를 가리킬지
            self.rear.next = node
            self.rear = node # 노드를 먼저 가리키면 주소 날아감 / 윗줄 아랫줄 순서 바뀌면

        self.size += 1

    def add(self, pos, data):
        node = Node(data, None, None) # previous, next 는 None으로 초기화 > 나중에 결정

        if pos == 1:
            self.addFront(data)

        elif pos == self.size + 1: # 제일 마지막으로 들어오는 거
            self.addRear(data)

        else:
            p = self.front

            for i in range(1, pos):
                p = p.next
                # 내가 가리키는 것
                node.prev = p.prev # 내 왼쪽은 p.prev
                node.next = p # 내 오른쪽은 p
                # 나를 가리키는 것
                p.prev.next = node
                p.prev = node

            self.size += 1

        # if pos == 0:
        #     self.addFront(data)

        # elif pos == self.size:
        #     self.addRear(data)

        # else:
        #     p = self.front

        #     for i in range(pos - 1):
        #         p = p.next

        #     node = Node(data, p, p.next)
        #     p.next.prev = node
        #     p.next = node

        #     self.size += 1

    def display(self):
        p = self.front

        while p != None:
            print('[%s] -> ' % p.data, end = '')
            p = p.next
        print('\b\b\b    ')

if __name__ == '__main__':
    DL = DoubleLinkedType()

    DL.addFront('Apple'); DL.addFront('Carrot')
    DL.addRear('Blueberry'); DL.addRear('Fig'); DL.display(); input()

    DL.add(1, 'Kiwi'); DL.add(DL.size + 1, 'Honeydew')
    DL.add(3, 'Melon'); DL.display()

#    delete first delete rear delete pos 은 셤공부 한다 생각하고 직접 해보기