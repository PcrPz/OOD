print(" *** String count *** ")
message = input("Enter message : ")
uppercase_count = 0
lowercase_count = 0
uppercase_chars = set()
lowercase_chars = set()

for char in message:
    if char.isupper():
            uppercase_count += 1
            uppercase_chars.add(char)
    elif char.islower():
            lowercase_count += 1
            lowercase_chars.add(char)

print("No. of Upper case characters :", uppercase_count)
print("Unique Upper case characters :", '  '.join(sorted(uppercase_chars)))
print("No. of Lower case Characters :", lowercase_count)
print("Unique Lower case characters :", '  '.join(sorted(lowercase_chars)))