from ArrayStack import ArrayStack

# 연산자가 전달되면, 연산자의 우선순위를 비교 후 반환
def precedence(op):
    if (op == '(' or op == ')'):   return 0
    elif (op == '+' or op == '-'): return 1
    elif (op == '*' or op == '/'): return 2

def infixToPostfix(expr):
    S = ArrayStack()
    postfix = [] # 후위 표기식으로 변환된 결과를 저장할 리스트 (EvalPostfix 전달 용도)

    for term in expr:
        if term in '+-*/':
            # 피연산자는 바로 집어 넣는 건 아니고, 스택이 비어 있지 않으면,
            while not S.isEmpty():
                op = S.peek()
                if(precedence(term) <= precedence(op)): # 스택의 top에 있는 연산자의 우선순위가 더 크거나 같으면
                    # postfix.append(S.pop()) :: 아래 두 줄 코드 한 줄로 압축 가능
                    postfix.append(op)
                    S.pop()
                else: break # 반복문 빠져 나오기
            S.push(term) # 스택에 연산자를 넣어줌

        elif term in '(': # 여는 괄호는 무조건 스택에 넣어줌
            S.push(term) # 스택에 연산자를 넣어줌

        elif term in ')': # 닫는 괄호는 여는 괄호가 나올 때까지 스택에서 pop 해줌
            while not S.isEmpty(): # 스택이 비어 있지 않다면, (근데 비어 있을 일은 없음)
                op = S.pop()
                if op == '(': break # 왼쪽 괄호면 그냥 스택 끝내면 됨 (반복문 빠져나오기)
                
                else: # 연산자(왼쪽 괄호가 아니면)면 후위 표기식에 추가해줌 >> 무조건 수식에 표기해야 함
                    postfix.append(op)

        else: # 피연산자이면 바로 출력 (후위 표기식에 추가)
            postfix.append(term)

    # 수식 스캔 끝나면, 
    while not S.isEmpty():
        postfix.append(S.pop()) # 스택에는 무조건 하나 이상의 연산자가 들어 있음. 그걸 다 꺼내서 후위 표기식에 추가해줌
    
    return postfix

if __name__ == '__main__':
    infix = input("Input Infix Expression: ")
    expr = infix.split()
    
    # 후위 표기식으로 변환
    postfix = infixToPostfix(expr)

    print("Infix Expression: ", infix) # 잘 입력 받았는지 확인 !: 입력받은 중위 표기식 출력
    print("Postfix Expression: ", postfix) # 후위 표기식 출력
    print(EvalPostfix(postfix)) # 후위 표기식을 계산해서 결과 출력

# 케이스 테스트 할 때 공백 잘 넣어 줘야 함