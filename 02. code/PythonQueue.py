import queue

Q = queue.Queue(maxsize=20) # 큐 클래스 객체에서 maxsize라는 queue 파라미터 지정
for v in range(1, 10):
    Q.put(v) # put() 메소드로 큐에 데이터 삽입 (enqueue, dequeue 말구)

print ("Queue: ", end='')
for v in range(1, 10):
    print (Q.get(), end='') # get() 메소드로 큐에서 데이터 추출 (dequeue)
print()

S = queue.LifoQueue(maxsize=20) # 큐 클래스 객체에서 maxsize라는 queue 파라미터 지정
for v in range(1, 10):
    S.put(v) # put() 메소드로 큐에 데이터 삽입 (enqueue, dequeue 말구)

print ("Stack: ", end='')
for v in range(1, 10):
    print (S.get(), end='') # get() 메소드로 큐에서 데이터 추출 (dequeue)
print()

# 주의사항: built in 으로 주어지는 것이니 쉽게 사용 가능하지만, 중간고사 때 빌트인 모듈을 사용하면 점수 없음. ...
# 중간고사 이후 트리 구조에서