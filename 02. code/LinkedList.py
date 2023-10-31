class Node: # StackType을 위한 재료 (구슬로 이루어진 목걸이에서 구슬 역할)
    def __init__(self, data, next): # linked field name: next
        self.data = data # reset
        self.next = next #

class ListType:
    def __init__(self):
        self.head = None # 스택 초기화 (= None)
        self.size = 0    # 노드의 개수

    def isEmpty(self):  # def isFull: 은 의미가 없음
        return self.head == None
    
    def getNode(self, pos):
        p = self.head
        # invalid pos. check (1번부터 self.size +1 까지)

        if pos == 1: # 이전 노드는 없음
            return None
        else:
            for i in range(1, pos - 1):
                p = p.next

            return p

    def insert(self, pos, data):
        before = self.getNode(pos) # position

        if before == None:
            self.head = Node(data, self.head)
        else:
            node = Node(data, before.next)
            before.next = node

        self.size += 1

    def delete(self, pos):
        # 생략 # if (pos <1 or pos > self.size): (포지션 위치가 잘 들어왔다는 조건 하에)
        if (not self.isEmpty()):
            before = self.getNode(pos)

            if before == None: # 첫 노드를 삭제한다는 의미, (이전 노드 없음)
                self.head = self.head.next
            else: 
                before.next = before.next.next
            self.size -= 1
            
        else:
            self.head = self.head.next
            self.size -= 1

    def display(self):
        p = self.head

        while p != None:
            print('[%s] -> ' % p.data, end = '')
            p = p.next

        print('\b\b\b     ')

if __name__ == '__main__':
    L = ListType()
    L.insert(1, 'A'); L.insert(1, 'C'); L.insert(L.size + 1, 'D');
    L.insert(2, 'F'); L.display()