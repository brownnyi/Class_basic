class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        print(self.result)

cal1 = Calculator()
cal2 = Calculator()

cal1.add(3)
cal1.add(5)
cal2.add(2)
cal2.add(4)

#RESULT
3
8
2
6
