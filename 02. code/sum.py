def sum_range(begin, end, step = 1):
    sum = 0
    # for n in range(begin, end + 1, step):
    for n in range(begin, end, step):
        sum += n
    return sum

if __name__ == '__main__': # if 문 안 구문 명령은, 지금 파일 (sum.py) 파이썬 파일에서 실행 시킬 때만 실행, 외부에서 끌어서 실행시키면 if 문 안 구문은 실행되지 않음
    print('Sum = ', sum_range(1, 11)) # 1부터 10까지 정수의 합
    print('Sum = ', sum_range(1, 11, 2)) # 1부터 10까지 홀수의 합
    print('Sum = ', sum_range(step=3, begin=1, end=11)) # 1 4 7 10 의 합

