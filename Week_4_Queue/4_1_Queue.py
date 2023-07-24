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
        
    def peek(self,pos):
        return self.queue[pos-1] if not self.is_empty() else None
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def __len__(self):
        return len(self.queue)
    
    def __str__(self):
        if not self.is_empty():
            return f"{', '.join(str(x) for x in self.queue)}"
        else:
            return "Empty"
    
    
    
    
massage = input("Enter Input : ").split(",")
queue = Queue()
temp = Queue()
i=0
for obj in massage:
    command=obj.split()
    if command[0] == "E":
        queue.enqueue(int(command[1]))
        print(*queue.queue, sep=', ')
    elif command[0] == "D":
        if not queue.is_empty():
            temp.enqueue(queue.dequeue())
            i+=1
            print(f"{temp.peek(i)} <- {queue}")
        else:
            print("Empty")
print(f"{temp} : {queue}")


    
    