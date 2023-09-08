class Queue:
    def __init__(self):
        self.queue=[]
    
    def enqueue (self,data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)
        
    def peek(self):
        return self.queue[0] if not self.is_empty() else None
        
    def is_empty(self):
        print(len(self.queue) == 0)
    
    def __len__(self):
        return len(self.queue)
    
    def __str__(self) -> str:
        if self.is_empty:
            return f"{', '.join(str(x) for x in self.queue)}"
        else:
            return f"Empty"
        

class Queue:
    def __init__ (self):
        self.queue = []

    def __len__(self):
        return len(self.queue)
    
    def is_empty(self):
        return (len(self.queue) == 0)
    
    def enqueue(self,data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty:
            return None
        else:
            return self.queue.pop(0)
    
    def __str__ (self):
        return f"{', '.join(str(x) for x in self.queue)}"
    
class Stack:
    def __init__ (self):
        self.stack =[]

    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return (len(self.stack)==0)
    
    def push(self,data):
        if self.is_empty():
            None
        else:
            self.stack.append(data)

    def pop(self):
        self.stack.pop()

    def peek(self):
        if self.is_empty():
            None
        else:
            return(self.stack[-1])
        
massage = list(map(str,input("enter number").split(",")))
print(massage)