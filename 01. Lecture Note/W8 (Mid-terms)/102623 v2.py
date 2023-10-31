import random

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SortedSet:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def makeSet(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1

        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            self.size += 1

        return self.head
    
    def intersect(self, S1, S2):
        curl = S1.head
        curr = S2.head
        while curl != None and curr != None:
            if curl.data == curr.data:
                self.makeSet(curl.data)
                curl = curl.next
                curr = curr.next
            elif curl.data < curr.data:
                curl = curl.next
            else:
                curr = curr.next

        curr = self.head
        while curr != None:
            curl = curr.next
            while curl != None:
                if curr.data > curl.data:
                    curr.data, curl.data = curl.data, curr.data
                curl = curl.next
            curr = curr.next

        return self.head

    def union(self, S1, S2):
        curl = S1.head
        curr = S2.head
        while curl != None and curr != None:
            if curl.data == curr.data:
                self.makeSet(curl.data)
                curl = curl.next
                curr = curr.next
            elif curl.data < curr.data:
                self.makeSet(curl.data)
                curl = curl.next
            else:
                self.makeSet(curr.data)
                curr = curr.next
        while curl != None:
            self.makeSet(curl.data)
            curl = curl.next
        while curr != None:
            self.makeSet(curr.data)
            curr = curr.next
        return self.head

    def difference(self, S1, S2):
        curl = S1.head
        curr = S2.head
        while curl != None:
            if curl.data != curr.data:
                self.makeSet(curl.data)
            curl = curl.next
        return self.head
    
    def display(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.next
        print()

if __name__ == '__main__':
    S1 = SortedSet()
    S2 = SortedSet()

    for i in range(10):
        S1.makeSet(random.randint(1, 30))
        S2.makeSet(random.randint(1, 30))

    print('Set 1 = ', end=''); S1.display()
    print('Set 2 = ', end=''); S2.display()

    S3 = SortedSet()
    S3.intersect(S1, S2)
    print('Inter = ', end=''); S3.display()

    S3.union(S1, S2)
    print('Union = ', end=''); S3.display()

    S3.difference(S1, S2)
    print('Diff = ', end=''); S3.display()