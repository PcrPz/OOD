class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1] if not self.isEmpty() else None
    
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self) -> str:
        return f"Value in Stack = {self.items}"
    
def manageStack(str):
    stack = Stack()
    temp = Stack()
    for com in str:
        com = com.split()
        if com[0] == "A":
            stack.push(int(com[1]))
            print(f"Add = {com[1]}")
        elif com[0] == "P":
            if stack.isEmpty():
                print("-1")
            else:
                print(f"Pop = {stack.pop()}")
        elif com[0] == "D":
            if stack.isEmpty():
                print("-1")
            else:
                while(not stack.isEmpty()):
                    if stack.peek() == int(com[1]):
                        print(f"Delete = {stack.pop()}")
                    else:
                        temp.push(stack.pop())
                while(not temp.isEmpty()):
                    stack.push(temp.pop())
        elif com[0] == "LD":
            if stack.isEmpty():
                print("-1")
            else:
                while(not stack.isEmpty()):
                    if stack.peek() < int(com[1]):
                        print(f"Delete = {stack.peek()} Because {stack.peek()} is less than {int(com[1])}")
                        stack.pop()
                    else:
                        temp.push(stack.pop())
                while(not temp.isEmpty()):
                    stack.push(temp.pop())
        elif com[0] == "MD":
            if stack.isEmpty():
                print("-1")
            else:
                while(not stack.isEmpty()):
                    if stack.peek() > int(com[1]):
                        print(f"Delete = {stack.peek()} Because {stack.peek()} is more than {int(com[1])}")
                        stack.pop()
                    else:
                        temp.push(stack.pop())
                while(not temp.isEmpty()):
                    stack.push(temp.pop())                                    
    print(stack)

     
massage = input("Enter Input : ").split(",")
manageStack(massage)