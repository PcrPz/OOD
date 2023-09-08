class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linked_list:
    def __init__(self, head = None):
        if head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            cur = self.head
            self.size = 1
            while cur.next is not None:
                cur = cur.next
                self.size += 1
            self.tail = cur

    def __str__(self):
        cur = self.head
        massage = ''
        while cur is not None:
            massage += str(cur.data)+'->'
            cur = cur.next
        return massage[:-2]
    #append
    def append(self,data):
        new_node = node(data)
        if self.size == 0:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        self.size += 1
    #บวกหัว
    def addHead(self,data):
        cur = node(data)
        if self.size == 0:
            self.append(data)
        else:
            cur.next = self.head
            self.head = cur
            self.size += 1

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            cur = self.head
            while cur != None and cur.next.data != data:
                cur = cur.next
                if cur.next is None:
                    return
        cur.next = cur.next.next
        self.size -= 1
    
    def nodeAt(self,i):
        cur = self.head
        for j in range(i):
            cur = cur.next
        return cur
    
    def search(self,data):
        cur = self.head
        while cur is not None:
            if str(cur.data) == str(data):
                return cur
            cur = cur.next
        return
    
Bokies = []
List_bokies = []
ans_list = []
count = -1
num = 0
inp = [[y for y in x.split(',')] for x in input("Enter input: ").split(' ')]
#loop add bokie
for i in range(1,(int(inp[0][0]))+1):
    Bokies.append(str(i))
#loop check bokies coming and check less more
for i in inp[1]:
    link = linked_list()
    boky_com = i.split('-')
    if boky_com[0] != boky_com[1]:
        link.addHead(boky_com[0])
        link.append(boky_com[1])
        count += 1
        if count != len(inp[1]):
            change_ll = True
            j = -1
            while change_ll == True:
                j += 1
                boky_con = inp[1][j].split('-')
                if boky_com[0] == boky_con[1] and boky_com[0] != boky_con[0]:
                    link.addHead(boky_con[0])
                    boky_com[0] = boky_con[0]
                    j = -1
                elif boky_com[1] == boky_con[0] and boky_com[1] != boky_con[1]:
                    link.append(boky_con[1])
                    boky_com[1] = boky_con[1]
                    j = -1
                elif j == len(inp[1])-1:
                    change_ll = False
            if len(List_bokies) == 0:
                List_bokies.append(str(link))
            else:
                token = 0
                for k in List_bokies:
                    if str(link).split('->')[0] in str(k.split('->')):
                        break
                    else:
                        token += 1
                    if token == len(List_bokies):
                        List_bokies.append(str(link))
for x in Bokies:
    appear_node = False
    for y in List_bokies:
        if int(x) == int(y.split('-')[0]):
            appear_node = True
            ans_list.append(y)
            break
        if x in y.split('->'):
            appear_node = True
    if appear_node == False:
        ans_list.append(x)
for i in ans_list:
    num += 1
    print(f'{num}: {i}')
print(f'Number of train(s): {num}')
