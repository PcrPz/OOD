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
        return "".join(self.items)

def wood(mas):
    stack = Stack()
    temp = Stack()
    for com in mas:
        com = com.split()
        if com[0] == "A":
            while not stack.isEmpty() and stack.peek() <= int(com[1]):
                stack.pop()
            stack.push(int(com[1]))
        elif com[0] == "B":
            print(stack.size())                  
    
massage = input("Enter Input : ").split(",")
wood(massage)
