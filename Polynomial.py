class ArrayList:
    def __init__(self):
        self.capacity = 10  # 초기 용량
        self.array = [None] * self.capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def insert(self, pos, e):
        if self.is_full():
            self.resize()

        if 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1
            return e
        else:
            print("Overflow or Invalid Position")

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def display(self):
        for i in range(self.size):
            print(self.array[i], end='')
        print()

    def delete(self, pos):
        if not self.is_empty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e
        else:
            print("Underflow or Invalid Position")


class Polynomial:
    def __init__(self):
        self.coef = ArrayList()

    def degree(self):
        return self.coef.size - 1 if not self.coef.is_empty() else 0

    def eval(self, scalar):
        result = 0
        for i in range(self.coef.size):
            result += self.coef.array[i] * (scalar ** i)
        return result

    def add(self, other):
        result = Polynomial()

        max_size = max(self.coef.size, other.coef.size)
        for i in range(max_size):
            coef1 = self.coef.array[i] if i < self.coef.size else 0
            coef2 = other.coef.array[i] if i < other.coef.size else 0
            result.coef.insert(i, coef1 + coef2)

        return result

    def display(self, label="P(x) = "):
        for i in range(self.coef.size):
            coef_str = "{:.0f}".format(self.coef.array[i])
            power_str = str(i)
            term = coef_str + "x^" + power_str

            print(term, end="")
            if i != 0:
                print(" + ", end="")
        print()

    def read(self):
        coef_str = input("Input degrees in order : ")
        coef_list = [float(coef) for coef in coef_str.split()]

        for i in range(len(coef_list) - 1, -1, -1):
            self.coef.insert(0, coef_list[i])


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
