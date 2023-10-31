class Node: # StackType을 위한 재료 (구슬로 이루어진 목걸이에서 구슬 역할)
    def __init__(self, data, next): # linked field name: next
        self.data = data # reset
        self.next = next #

class StackType:
    def __init__(self):
        self.top = None # 원래는 이름을 head라고 하는데 여기서는 stack을 만드는 거라 이름은 'top'으로 함
                        # 스택 초기화 (= None)
        self.size = 0   # 노드의 개수

    def isEmpty(self):  # def isFull: 은 의미가 없음
        return self.top == None
    #    return self.size == 0 # 둘 중 하나
    
    def push(self, data): # insertFirst() 함수와 같은 의미 # 각각 함수가 뭘 의미하는지는 기억하고 있는 게 좋겟죵 ?
        node = Node(data, None) # 새로운 노드 생성
        node.next = self.top    # 새로운 노드의 next가 top을 가리키게 함
        self.top = node         # top이 새로운 노드를 가리키게 함 (나는 누굴 가리켜?)
        self.size += 1          # 노드의 개수를 하나 증가시킴

    def pop(self): # deleteFirst()
        if not self.isEmpty():
            p = self.top
            data = p.data
            self.top = p.next
            self.size -= 1
            return data

        else: pass

    def peek(self): # getFirst()
        if not self.isEmpty():
            return self.top.data
        else: pass

    def display(self):
        p = self.top

        while p != None:
            print('[%s] -> ' % p.data, end = '')
            p = p.next

        print('\b\b\b     ')
            

if __name__ == '__main__': # test
    S = StackType()
    S.push('B'); S.push('C'); S.push('A');
    S.display() # A C B

    print('Pop: %s' %S.pop()); S.display()
    print('Peek: %s' %S.peek()); S.display()