from Polynomial import Polynomial

coef = []
degree = 0

def degree():
    return degree

def eval(scalar):
    result = 0
    for i in range(len(coef)):
        result += coef[i] * (scalar ** i)
    return result

def add(other):
    c = Polynomial()

    if len(coef) > len(other.coef):
        c.coef = coef[:]
        for i in range(len(other.coef)):
            c.coef[i] += other.coef[i]
    
    else:
        c.coef = other.coef[:]
        for i in range(len(coef)):
            c.coef[i] += coef[i]
    
    return c

def display():
    for i in range(len(coef)):
        print("%5.1f x^%d" % (coef[i], i), end="")
        if i != len(coef) - 1:
            print(" + ", end="")
    print()

def read():
    degree = int(input("Input degrees in order: "))
    for i in range(degree + 1):
        coef.append(float(input("Enter coefficient of x^%d: " % i)))

if __name__ == '__main__':
    a = Polynomial()
    b = Polynomial()

    a.read()
    b.read()

    c = a.add(b)

    a.display("A(x) = ")
    b.display("B(x) = ")
    c.display("C(x) = ")

    print("C(2) = ", c.eval(2))