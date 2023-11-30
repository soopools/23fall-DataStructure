from ArrayStack import ArrayStack

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
    postfix = '8 2 / 3 - 3 2 * +'
    expr = postfix.split()

    print(postfix, ' ---> ', evalPostfix(expr))