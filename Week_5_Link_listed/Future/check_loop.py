class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.visited = False

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self,data):
        newNode = Node(data)
        if self.head == None :
            self.head = newNode
            self.tail = newNode
            