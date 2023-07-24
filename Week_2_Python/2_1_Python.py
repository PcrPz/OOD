class Calculator:
    def __init__(self,x):
        self.value = x
    
    def __add__(self,y):
        return int(self.value+y.value)

    def __sub__(self,y):
        return int(self.value-y.value)

    def __mul__(self,y):
        return int(self.value*y.value)

    def __truediv__(self,y):
        return float(self.value/y.value)
    
x,y = input("Enter num1 num2 : ").split(",")
x,y = Calculator(int(x)),Calculator(int(y))
print(f"{x+y}\n{x-y}\n{x*y}\n{x/y}\n")