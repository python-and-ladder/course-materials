class Calculator:
    def add(self, a, b):
        print("Adding two numbers")
        return a + b

    def add(self, a, b, c=0):
        print("Adding three numbers")
        return a + b + c

c = Calculator()

c.add(2, 3)
c.add(2, 3, 4)