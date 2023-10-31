class ArrayList: # 1. 클래스 선언

    # 2. 전역변수 > 멤버 변수로 변환
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    
    def isEmpty(self):
        return self.size() == 0