class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class Doublylink:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size ==0

    def add_station(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.head.prev = new_node
            self.head.next =new_node
        else:
            tail = self.head.prev
            new_node.next =self.head
            new_node.prev = tail
            self.head.prev = new_node
            tail.next = new_node
    
    def route (self,start,stop,direct=None):
        path_front = []
        path_back = []
        num_front = 0
        num_back = 0
        if direct == "F":
            start = self.search(start)
            stop = self.search(stop)
            cur_node = start
            while cur_node != stop:
                num_front +=1
                path_front.append(cur_node.data)
                cur_node = cur_node.next
            path_front.append(cur_node.data)
            print(f'Forward Route: {"->".join(path_front)},{num_front}')


        elif direct == "B":
            start = self.search(start)
            stop = self.search(stop)
            cur_node = start
            while cur_node != stop:
                num_back +=1
                path_back.append(cur_node.data)
                cur_node = cur_node.prev
            path_back.append(cur_node.data)
            print(f'Backward Route: {"->".join(path_back)},{num_back}')


        elif direct == None:
            start = self.search(start)
            stop = self.search(stop)
            cur_node = start
            while cur_node != stop:
                num_front +=1
                path_front.append(cur_node.data)
                cur_node = cur_node.next
            path_front.append(cur_node.data)
            cur_node = start
            while cur_node != stop:
                num_back +=1
                path_back.append(cur_node.data)
                cur_node = cur_node.prev
            path_back.append(cur_node.data)
            if num_front > num_back:
                print(f'Backward Route: {"->".join(path_back)},{num_back}')
            elif num_front< num_back:
                print(f'Forward Route: {"->".join(path_front)},{num_front}')
            else:
                print(f'Forward Route: {"->".join(path_front)},{num_front}')
                print(f'Backward Route: {"->".join(path_back)},{num_back}')
        
    
    def search (self,data):
        cur_node = self.head
        while cur_node != self.head.prev:
            if data == cur_node.data:
                return cur_node
            cur_node = cur_node.next
        if data == cur_node.data:
            return cur_node


platforms = Doublylink()
print("***Railway on route***")
massage = input("Input Station name/Source, Destination, Direction(optional): ").split("/")
station = massage[0].split(",")
com = massage[1].split(",")
for y in station :
    platforms.add_station(y)
platforms.route(*com)



