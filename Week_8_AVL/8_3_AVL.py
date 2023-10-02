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
        def insertion(root, data):
            if not root:
                root = Node(data)
            elif root.data > data:
                root.left = insertion (root.left, data)
            elif root.data <= data:
                root.right = insertion(root.right, data)
            return root
        self.root = insertion(self.root, data)
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
        
    def ranking(self,checknum):
        def ranking_(root,checknum):
            if root == None:
                return 0
            if checknum >= root.data:
                return ranking_(root.left,checknum) + ranking_(root.right,checknum) + 1
            if checknum < root.data:
                return ranking_(root.left,checknum)
        rankingNum = ranking_(self.root,checknum)
        return print(f"Rank of {checknum} : {rankingNum}")
            
    
    
T = BST()
mes,checknum = input('Enter Input : ').split("/")
inp = [int(i) for i in mes.split()]
for i in inp:
    T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------")
T.ranking(int(checknum))