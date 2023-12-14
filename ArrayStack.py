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
