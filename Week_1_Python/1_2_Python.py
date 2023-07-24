print("*** multiplication or sum ***")
a, b =input("Enter num1 num2 : ").split()
result = int(a)*int(b)
if result > 1000:
    print("The result is",int(a)+int(b)) 
else:print("The result is", result)
