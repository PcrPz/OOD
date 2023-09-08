class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def append(root,data):
            if root == None:
                root = Node(data)
            elif data < root.data:
                root.left = append(root.left,data)
            elif data >= root.data:
                root.right = append(root.right,data)
            return root
        self.root = append(self.root,data)
        return self.root
        
            
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def find_below(self,belowN):
        def watchN(root,belowN,lessList):
            if root == None:
                return lessList
            elif belowN > root.data:
                lessList.append(str(root.data))
            return watchN(root.left,belowN,[]) + lessList  + watchN(root.right,belowN,[])
        return watchN(self.root,belowN,[])  
    
    
    
        

T = BST()
inputC,belowN = input('Enter Input : ').split("|")
inp = [int(i) for i in inputC.split()]
for i in inp:
    root = T.insert(i)
belowGroup = T.find_below(int(belowN))
T.printTree(root)
print("--------------------------------------------------")
if belowGroup == []:
    print(f"Below {belowN} : Not have")
else:
    print(f"Below {belowN} : {' '.join(belowGroup)}")