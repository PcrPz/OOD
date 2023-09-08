class Queue:
    def __init__ (self):
        self.queue =[]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def __len__(self):
        return len(self.queue)

    def dequeue(self):
        return self.queue.pop(0) if not self.is_empty() else None
    
    def enqueue(self,data):
        self.queue.append(data)


class MazeRunner:
    
    def __init__(self):
        self.queue = Queue()
        self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def find_start(self,room: list):
        for i in range(len(room)):
            for j in range(len(room[i])):
                if room[i][j] == "F":
                    return(j,i)
        return
                
    def find_the_next_move(self, room):
        x,y = self.queue.dequeue()
        for dx, dy in self.directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_y < len(room) and 0 <= new_x < len(room[0]) and room[new_y][new_x] == 'O':
                return True
            elif 0 <= new_y < len(room) and 0 <= new_x < len(room[0]) and room[new_y][new_x] == '_':
                self.queue.enqueue((new_x, new_y))
                room[new_y][new_x] = 'X'
                
                
    def search(self, width, height, room):
        x = self.find_start(room)
        if not x :
            return print('Invalid map input.')
        self.queue.enqueue(x)
        if  len(room) != int(height):
            return print("Invalid map input.")
            
        for row in room:
            if len(row) != int(width):
                return print("Invalid map input.")
        # Main Loop
        while not self.queue.is_empty():
            print(f'Queue: {self.queue.queue}')
            if self.find_the_next_move(room):
                print('Found the exit portal.')
                return
        return print('Cannot reach the exit portal.')


maze = []
width,height,room = input("Enter width, height, and room: ").split(" ")
room = [list(string) for string in room.split(',')]
maze_runner =MazeRunner()
maze_runner.search(width,height,room)

                
          
  