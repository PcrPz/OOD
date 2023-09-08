# 2D - Link List ( pri_node ไม่มีวันที่ pri_node ซ้ำกัน )

# ADN  : add pri_node
# ADSN : add sec_node

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.next_s = None

class Snode:
    def __init__(self,data):
        self.data = data
        self.next_s = None

class link:
    def __init__(self) -> None:
        self.head = None

    def next_node(self, val):
        new_node = val
        check = self.search(val.data)
        if check==None :
            if self.head != None:
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = new_node
            else:
                self.head = new_node
        else: return None

    def search(self,data):
        if self.head != None:
            temp = self.head
            while temp != None:
                if temp.data == data:
                    return temp
                temp = temp.next
        else:
            return None 


    def next_secondary_node(self,pri,val):
        new_node = val
        primal = self.search(pri)
        if primal !=None:
            if primal.next_s != None:
                temp = primal
                while temp.next_s != None:
                    temp = temp.next_s
                temp.next_s = new_node
            else:
                primal.next_s = new_node
        else: return None

    def show_all(self):
        if self.head == None:
            return None
        else:
            temp1 = self.head
            temp2 = self.head
            while temp1 != None:
                s =''
                temp2 = temp1
                while temp2.next_s!= None:
                    s += str(temp2.next_s.data) + ","
                    temp2 = temp2.next_s
                print(temp1.data+" : "+s)
                temp1= temp1.next


def main():
    inp = input("input : ").split(",")
    l = link()
    for i in inp:
        u = i.split(" ")
        if u[0] == "ADN":
            l.next_node(node(u[1]))
        elif u[0] == "ADSN":
            h = u[1].split("-")
            l.next_secondary_node(h[0],Snode(h[1]))
    l.show_all()
        
  

main()