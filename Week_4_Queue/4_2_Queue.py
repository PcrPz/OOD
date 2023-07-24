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
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def __len__(self):
        return len(self.queue)
    
    def __str__(self):
        if not self.is_empty():
            return f"{self.queue[0]}"
        else:
            return "Empty"




massage = input("Enter Input : ").split(",")
Normal = Queue()
Vip = Queue()
for obj in massage:
    command=obj.split()
    if command[0] == "EN":
        Normal.enqueue(command[1])
    elif command[0] == "ES":
       Vip.enqueue(command[1])
    elif command[0] == "D":
        if not Vip.is_empty():
            print(Vip.dequeue())
        else:
            if not Normal.is_empty():
                print(Normal.dequeue())
            else:
                print("Empty")
