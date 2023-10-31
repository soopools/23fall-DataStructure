# 1
# def iPower(x, n):
#    result = 1
#    for i in range (n):
#        result *= x
#    return result

# print('ipower: %d' %(iPower(2, 10)))

#result: 1024 (2^10)

# -- 이 문제를 순환문으로 풀어보자. (조건: 선형 시간복잡도보다 빠르게)
# 1-1 (시간복잡도를 선형보다 낮추는 유일한 방법)
# def iPower (x, n):
#     if n == 0:
#         return 1
#     elif (n % 2) == 0:
#         return rpower (x * x, n//2) # 재귀 호출
#     else:
#         return x * rpower(x*x, (n-1)//2)
    
#     print ('iPower: %d' % (iPower(2,10)))
#     print ('rPower: %d' % (rPower(2,10)))


# #2-1 피보나치 수열
# def rFib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return rFib(n-2) + rFib(n-1)
    
# print('rFib : %d' %(rFib(10)))
    
# #2-2 피보나치 수열 - 재귀 함수 호출 횟수 알려면 전역변수를 써야 함 (파이썬에서)
# count = 0 #전역변수 플밍 젤 윗 부분에 쓰기
# #전역변수 해놓으면 하나 전역변수를 전부 공유해서 사용, 변수 생명주기: 프로그래밍 끝날 때까지 메모리에서 사라지지 않음, 지속적인 사용 가능
# def rFib(n):
#     global count #변수가 함수 안에서 지역변수로 실행되면 함수 실행 마치고 변수가 사라짐 (변수 생명주기)
#     count += 1 #
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return rFib(n-2) + rFib(n-1)
    
# print('rFib : %d' %(rFib(10)))
    
# #2-3
# count = 0 #전역변수 플밍 젤 윗 부분에 쓰기
# #전역변수 해놓으면 하나 전역변수를 전부 공유해서 사용, 변수 생명주기: 프로그래밍 끝날 때까지 메모리에서 사라지지 않음, 지속적인 사용 가능
# def rFib(n):
#     global count #변수가 함수 안에서 지역변수로 실행되면 함수 실행 마치고 변수가 사라짐 (변수 생명주기)
#     count += 1

#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return rFib(n-2) + rFib(n-1)
    
# print('rFib : %d - count: %d' %(rFib(20), count))

# #2-4
# count = 0 #전역변수 플밍 젤 윗 부분에 쓰기
# #전역변수 해놓으면 하나 전역변수를 전부 공유해서 사용, 변수 생명주기: 프로그래밍 끝날 때까지 메모리에서 사라지지 않음, 지속적인 사용 가능
# def rFib(n):
#     global count #변수가 함수 안에서 지역변수로 실행되면 함수 실행 마치고 변수가 사라짐 (변수 생명주기)
#     count += 1

#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return rFib(n-2) + rFib(n-1)
    
# def iFib(n):
#     if (n < 2):
#         return n
    
#     pp = 0
#     p = 1

#     for i in range(2, n+1):
#         current = p + pp #current
#         pp = p
#         p = current
    
#     return current

# print('rFib : %d - count: %d' %(rFib(20), count))
# print('iFib : %d' %(iFib(500)))
    

#3-1 하노이탑
def hanoi(n, fr, tmp, to): #from은 파이썬 예약어얌

    if (n == 1): #원반이 하나만 남았을 때
        print ('Disk %d: %s --> %s' %(n, fr, to)) #fr: from의 역할을 하는 기둥의 이름, to: to의 역할을 하는 기둥의 이름
    else:
        hanoi (n-1, fr, to , tmp)
        print ('Disk %d: %s --> %s' %(n, fr, to))
        hanoi (n-1, tmp, fr, to)

hanoi(4, 'A', 'B', 'C')