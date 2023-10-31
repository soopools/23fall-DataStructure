class Polynomial:
    def __init__(self):
        self.coef = []

    def read(self):
        self.coef = [float(x) for 
        x in input().split()]

    def display(self, msg="f(x) = "):
        print(msg, end="")
        for i in range(len(self.coef)):
            print("%5.1f x^%d" % (self.coef[i], i), end="")
            if i != len(self.coef) - 1:
                print(" + ", end="")
        print()

    def add(self, b):
        c = Polynomial()
        if len(self.coef) > len(b.coef):
            c.coef = self.coef[:]
            for i in range(len(b.coef)):
                c.coef[i] += b.coef[i]
        else:
            c.coef = b.coef[:]
            for i in range(len(self.coef)):
                c.coef[i] += self.coef[i]
        return c

    def eval(self, x):
        result = 0
        for i in range(len(self.coef)):
            result += self.coef[i] * (x ** i)
        return result



if __name__ == '__main__':
    a = Polynomial()
    b = Polynomial()

    a.read()
    b.read()
    c = a.add(b)

    a.display("A(x) = ")
    b.display("B(x) = ")
    c.display("C(x) = ")

    print("c(2) = ", c.eval(2))