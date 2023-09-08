class Node():
    def __init__(self,data=None):
        self.data = data
        self.next =None
        self.prev = None
    
class Doublylink():
    def __init__(self) -> None:
        self.head =Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size =0
        self.alpha = False

    def is_empty(self):
        return self.size == 0 
    
    def append(self,data):
        new_node = Node(data)
        before_tail = self.tail.prev
        new_node.prev = before_tail
        new_node.next = self.tail
        before_tail.next = new_node
        self.tail.prev = new_node
        self.size += 1
        if data.isalpha():
            self.alpha = True

    def __str__(self):
        if self.is_empty():
            return "Empty"
        message = []
        cur_node = self.head.next 
        while cur_node != self.tail:
            message.append(cur_node.data)
            cur_node = cur_node.next
        if self.alpha:
            return " > ".join(message)
        else:
            return " <-> ".join(message)
        
    def reverse(self,k):
        cur = self.head.next
        temp = None
        while cur != self.tail:           
            first = cur 
            for i in range(k):
                t = cur.next
                cur.next = cur.prev
                cur.prev = t
                last = cur
                cur = cur.prev
                if cur == self.tail:
                    break
            if not temp:
                self.head.next = last
                last.prev = self.head
            else:
                temp.next = last
                last.prev = temp
            first.next = cur
            temp = first


def main():
    link = Doublylink() 
    element,size =input("Enter the elements of Linked list/group's size: ").split("/")
    for i in element.split():
        link.append(i)
    if link.is_empty():
        print("No elements in Linked List ? OK!")
        print("Group' size should be greater than 0")
        return 0
    if int(size) <= 0:
        return print("Group' size should be greater than 0")
    print()
    print(f"Original Linked list: {link}")
    link.reverse(int(size))
    print(f"Modified Linked list: {link}")



main()

    