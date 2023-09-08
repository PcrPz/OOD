class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Linklist():
    def __init__(self) -> None:
        self.head = self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def append(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size +=1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size +=1
    
    def pop(self):
        if self.is_empty():
            return print("No Data to PoP")
        else:
            cur = self.head
            while(cur.next.next != None):
                cur = cur.next
            prev = cur
            prev.next =None
            self.tail = prev
            self.size -= 1

    def addhead(self,data):
        new_node= Node(data)
        if self.is_empty():
            return self.append()
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
        
    def search1(self,data):
        cur = self.head
        index = 0
        if self.is_empty():
            return print("No Search")
        else:
            while(cur.next != None):
                if cur.data == str(data):
                    return print(index)
                cur = cur.next
                index = index +1
            return print("No Data")
    
    def search2(self,item):
        cur = self.head
        index = 0
        if  self.is_empty():
            return print("No Search")
        else:
            while cur.next != None:
                if cur.data == item:
                    return print(index)
                cur = cur.next
                index += 1
        return print("Not Found")
            

            

    def __str__(self) -> str:
        if self.is_empty():
            return print(f"No Data in LinkListed")
        else:
            cur = self.head
            s='Data in LinkListed: '
            while cur.next != None:
                s = s + str(cur.data+" ")
                cur = cur.next
            s = s + str(cur.data+" ")
            return s


ll = Linklist()
ll.append("-1")
ll.append("-2")
ll.append("1")
ll.addhead("5")
ll.search1("5")
ll.search2("-1")
print(ll)
