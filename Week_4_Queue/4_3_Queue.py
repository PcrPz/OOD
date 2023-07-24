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
            return f"{self.queue}"
        else:
            return "Empty"
        
list_q = Queue()
massage, hint = input("Enter code,hint : ").split(",")
num = ord(hint) - ord(massage[0])
#find hint
for i in massage:
    new_ascii= ord(i)+ num
    new_alpha = chr(new_ascii)
    list_q.enqueue(new_alpha)
    print(list_q)
    # ord(massage[0])