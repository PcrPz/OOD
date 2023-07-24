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
        
q = Queue()
q.is_empty
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.is_empty
    