class ArrayStack:

    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity - 1
    
    def push(self, data):
        if self.isFull():
            raise Exception("Stack is full")
        self.top += 1
        self.array[self.top] = data

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        data = self.array[self.top]
        self.top -= 1
        return data

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.array[self.top]
    
    ''' 
    10/5/23 수업시간 추가, 겨수님 이런 거 시험 문제 내는 거 좋아하심 ,ㅜ

    def sortedPush(self, e):
        if:
            self.push(e)
        
        else:
            while not self.isEmpty():
                if e < self.peek():
                    self.push(e)
                    break
                else:
                    self.push(self.pop())
            else:
                self.push(e)

    # element는 스택이 비었을 때 입력될 수 있음
    # 스택이 비어 있지 않으면, 스택의 top에 있는 항목과 비교해서,  ..  잠깐 옆에 치워 놓음 > 근데 이건 자동으로 댐
    '''

    # 교수님 풀이

    def sortedPush(self, e):
        if (self.isEmpty() or e < self.peek()):
            self.push(e)
        else:
            temp = self.pop()
            self.sortedPush(e)
            self.push(temp)

    def size(self):
        return self.top + 1
    
    def __str__(self):
        return str(self.array[:self.top + 1])
    
    def __repr__(self):
        return str(self.array[:self.top + 1])
    
    def __len__(self):
        return self.size() 
    
    def __iter__(self):
        for i in range(self.top, -1, -1):
            yield self.array[i]

# Path: EvalPostfix.py
# Compare this snippet from EvalPostfix.py:
# from ArrayStack import ArrayStack
def evalPostfix(expr):
    stack = ArrayStack()
    for token in expr:
        if token.isdigit():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = doMath(token, operand1, operand2)
            stack.push(result)
    return stack.pop()

if __name__== '__main__':
    S = ArrayStack(10)

    data = [5, 3, 8, 1, 2, 7]

    for d in data:
        S.sortedPush(d)
        S.display()