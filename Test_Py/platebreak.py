class Stack:
    def __init__ (self):
        self.stack =[]

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return self.size ==0
    
    def push(self,data):
        if self.is_empty:
            None
        else:
            self.stack.append(data)
    
    def pop(self):
        self.stack.pop()

    def peek(self):
        if self.is_empty:
            None
        else:
            self.stack[-1]

massage = list(map(str,input("Enter Input : ").split(",")))
print(massage)
stack =Stack()
for cur in massage:
    weight=int(cur.split()[0])
    fre=int(cur.split()[1])
    while not stack.is_empty() and stack.peek() < int(cur.split()[0]):
        print stack.peek().split()
        stack.pop()

stack.push(cur)
