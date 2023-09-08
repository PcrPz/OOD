def fibo(n):
    return n if n <= 1 else fibo(n-1)+fibo(n-2)
num =int(input("Enter Number : "))
print(f"fibo({num}) = {fibo(num)}")