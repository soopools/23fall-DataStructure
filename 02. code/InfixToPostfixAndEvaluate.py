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
            # 피연산자는 바로 집어 넣는 건 아니고, 스택이 비어 있지 않으면
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

def evalPostfix(expr): # 공백을 제외한 항을 입력으로 받는 클래스
    S = ArrayStack() # 스택 객체 생성

    # 날아온 수식
    for term in expr:
        if term in '+-*/': # 갖고 온 항목이 연산자라면 (이렇게 코딩할 수 있는 건 파이썬이라 ,,)
            op2 = S.pop() # 스택에서 두 번째 항목을 꺼내서
            op1 = S.pop() # 스택에서 첫 번째 항목을 꺼내서

            if   term == '+': S.push(op1 + op2) # 연산자에 따라서 연산을 수행하고
            elif term == '-': S.push(op1 - op2)
            elif term == '*': S.push(op1 * op2)
            elif term == '/': S.push(op1 / op2)
            # 맨 마지막은 else 로 해도 됨, 근데 줄 맞추려구 elif 로 함
            
        else:
            S.push(float(term)) 
            # 피연산자면 스택에 넣으면 됨
            # 스택에 집어 넣는 값은 8 2 3 3 2 이렇게 숫자가 들어가지만, 데이터 타입에 관한 정의를 해줘야 함 (모든 언어가 데이터 타입 맞춰주는 거 중요햄)
            # 나누기가 있으니까 float 으로 형변환
    
    # for 문 밖으로 빠져나오면 (모든 수식의 스캔이 끝나면)
    return S.pop() # 스택에 남아있는 마지막 항목이 최종 결과값이므로, 그걸 꺼내서 리턴해주면 됨

if __name__ == '__main__':
    # 잘 입력 받았는지 확인 !: 입력받은 중위 표기식 출력
    infix = input("Input Infix Expression: ")
    expr = infix.split()
    # print("Infix Expression: ", infix) # 위에 두 줄 이렇게도 표현 가능
    
    postfix = infixToPostfix(expr) # 후위 표기식으로 변환

    # 후위 표기식 출력
    print(evalPostfix(postfix)) # 후위 표기식을 계산해서 결과 출력
#   print("Postfix Expression: ", postfix) # 윗 줄이랑 결과 같음

# 케이스 테스트 할 때 공백 잘 넣어 줘야 함 !!