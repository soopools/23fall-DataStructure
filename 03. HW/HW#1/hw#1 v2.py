class Polynomial:
    
    def __init__(self):
        self.coef = []
        
    def degree(self):
        return len(self.coef) - 1
    
    def evaluate(self, scalar):
        result = 0
        for i in range(len(self.coef)):
            result += self.coef[i] * (scalar ** i)
        return result
    
    def add(self, other):
        c = Polynomial()
        if len(self.coef) > len(other.coef):
            c.coef = self.coef[:]
            for i in range(len(other.coef)):
                c.coef[i] += other.coef[i]
        else:
            c.coef = other.coef[:]
            for i in range(len(self.coef)):
                c.coef[i] += self.coef[i]
        return c
    
    def display(self, msg=""):
        print(msg, end="")
        for i in range(len(self.coef)):
            print("%5.1f x^%d" % (self.coef[i], i), end="")
            if i != len(self.coef) - 1:
                print(" + ", end="")
        print()
    
    def read(self):
        self.coef = [float(x) for x in input().split()]




if __name__ == '__main__':
    a = Polynomial()
    b = Polynomial()

    a.read()
    b.read()
    c = a.add(b)

    a.display("A(x) = ")
    b.display("B(x) = ")
    c.display("C(x) = ")

    print("c(2) = ", c.evaluate(2))
