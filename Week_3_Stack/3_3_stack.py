class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1] if not self.isEmpty() else None
    
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self) -> str:
        return "".join(self.items)
    
def candy_crush(mas):
    combo = 0
    stack=Stack()
    temp =Stack()

    for item in mas:
        if stack.isEmpty():
            stack.push(item)
        elif stack.items[-1] == item:
            stack.push(item)
            if stack.size() >= 3:
                if stack.items[-1] == stack.items[-2] == stack.items[-3]:
                    combo += 1
                    for _ in range(3):
                        stack.pop()
        else:
            stack.push(item)

    while not stack.isEmpty():
        color = stack.pop()
        temp.push(color)

    if temp.size() != 0:
        print(temp.size())
        print(temp)
        if combo > 1:
            print(f'Combo : {combo} ! ! !')
    else:
        print(temp.size())
        print("Empty")
        if combo > 1:
            print(f'Combo : {combo} ! ! !')

        
massage = input("Enter Input : ").split()
candy_crush(massage)
    