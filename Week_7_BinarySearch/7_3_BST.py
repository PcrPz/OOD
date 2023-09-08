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

    def lessThan(self,belowN):
        def watchN(root,belowN):
            count = 0
            if root == None:
                return count
            elif belowN >= root.data:
                count += 1
            return watchN(root.left,belowN) + watchN(root.right,belowN) + count
        return watchN(self.root,belowN)  
    
    
    
        

T = BST()
inputC,k = input('Enter Input : ').split("/")
inp = [int(i) for i in inputC.split()]
for i in inp:
    root = T.insert(i)
belowGroup = T.lessThan(int(k))
T.printTree(root)
print("--------------------------------------------------")
print(belowGroup)