def palin(n):
    if len(n)<=1:
        return "is palindrome"
    if n[0] != n[-1]:
        return "is not palindrome"
    return palin(n[1:-1])
message = input("Enter Input : ")
print(f"'{message}' {palin(message)}")