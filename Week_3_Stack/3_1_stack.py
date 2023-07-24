
massages = input("Enter Input : ").split(",")
stack = []
for string in massages:
    obj = string.split()
    if obj[0] == "A":
        stack.append(int(obj[1]))
        print(f"Add = {obj[1]} and Size = {len(stack)}")
    elif obj[0] == "P":
        if len(stack) == 0 :
            print("-1")
        elif len(stack) > 0 :
            print(f"Pop = {stack[len(stack)-1]} and Index = {len(stack)-1}")
            stack.pop()
if len(stack) == 0:
    print(f"Value in Stack = Empty")
else:
    print(f"Value in Stack =", *stack)
    

