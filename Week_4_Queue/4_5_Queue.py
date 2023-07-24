class Queue:
    def __init__ (self):
        self.queue =[]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def __len__(self):
        return len(self.queue)

    def dequeue(self):
        if self.is_empty():
            None
        else:
            self.queue.pop(0)
    
    def enqueue(self,data):
        self.queue.append(data)

def maze_runner(width,height,room):

    queue_find = Queue()
    for i in room.split(","):
        maze.append(list(i))
    print(len(maze))
    if height == "1" and width == "1":
        return print("Cannot reach the exit portal.")

    if len(maze) != height:
        return print("Invalid map input.")
        
    for layer in maze:
        if len(layer) != width:
            return print("Invalid map input.")
        
        for item in layer:
            if item
        
        
    
    

        


maze = []
width,height,room = input("Enter width, height, and room: ").split(" ")
print(room)
maze_runner(width,height,room)
